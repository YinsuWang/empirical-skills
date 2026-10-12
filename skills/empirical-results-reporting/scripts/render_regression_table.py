#!/usr/bin/env python3
"""Format verified estimates as Markdown, LaTeX and HTML regression tables.

No estimation, p-value calculation, or imputation. Python standard library only.
"""
import argparse
import csv
import html
import math
from dataclasses import dataclass
from pathlib import Path


def read_csv(path, required):
    with Path(path).open(encoding='utf-8-sig', newline='') as stream:
        reader = csv.DictReader(stream)
        fields = reader.fieldnames or []
        if not set(required).issubset(fields):
            raise ValueError(f'{path}: required columns: {required}')
        rows = list(reader)
    if not rows:
        raise ValueError(f'{path}: no data rows')
    return fields, rows


def number(value, field):
    if value is None or not value.strip():
        return None
    result = float(value)
    if not math.isfinite(result):
        raise ValueError(f'{field}: use blank for missing; got {value!r}')
    return result


def formatted(value, digits):
    if value is None:
        return '—'
    if value != 0 and abs(value) < 0.5 * 10 ** (-digits):
        return f'{value:.{digits}e}'
    return f'{value:.{digits}f}'


def stars(p):
    if p is None:
        return ''
    return '***' if p < .01 else '**' if p < .05 else '*' if p < .10 else ''


@dataclass(frozen=True)
class EstimateCell:
    value: str
    significance: str


def math_number(value):
    if 'e' in value.lower():
        mantissa, exponent = value.lower().split('e')
        return mantissa + r'\times 10^{' + str(int(exponent)) + '}'
    return value


def md(value):
    if isinstance(value, EstimateCell):
        if value.significance:
            body = math_number(value.value)
            if 'e' in value.value.lower():
                body = '{' + body + '}'
            return '$' + body + '^{' + value.significance + '}$'
        return value.value
    return str(value).replace('\n', ' ').replace('|', r'\|')


def tex(value):
    if isinstance(value, EstimateCell):
        return tex(value.value) + (r'\textsuperscript{' + value.significance + '}' if value.significance else '')
    escapes = {'\\': r'\textbackslash{}', '&': r'\&', '%': r'\%',
               '$': r'\$', '#': r'\#', '_': r'\_', '{': r'\{',
               '}': r'\}', '~': r'\textasciitilde{}', '^': r'\textasciicircum{}'}
    return ''.join(escapes.get(c, c) for c in str(value).replace('\n', ' '))


def html_cell(value):
    if isinstance(value, EstimateCell):
        return html.escape(value.value) + ('<sup>' + value.significance + '</sup>' if value.significance else '')
    return html.escape(str(value))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--estimates', required=True)
    parser.add_argument('--metadata', required=True)
    parser.add_argument('--output', required=True, help='Markdown file; matching .tex and .html also written')
    parser.add_argument('--title', required=True)
    parser.add_argument('--note', required=True, help='Actual sample, estimator and inference notes')
    parser.add_argument('--digits', type=int, default=3)
    args = parser.parse_args()
    if not 0 <= args.digits <= 10:
        parser.error('--digits must be between 0 and 10')
    if Path(args.output).suffix.lower() != '.md':
        parser.error('--output must end in .md')
    try:
        fields, meta = read_csv(args.metadata, ['model_id', 'column_label'])
        _, estimates = read_csv(args.estimates, ['model_id', 'term', 'label', 'coefficient', 'se', 'p_value'])
        models = [row['model_id'] for row in meta]
        if any(not m.strip() for m in models) or len(set(models)) != len(models):
            raise ValueError('metadata model_id must be nonempty and unique')
        if any(not row['column_label'].strip() for row in meta):
            raise ValueError('metadata column_label must be nonempty')
        terms, labels, lookup = [], {}, {}
        for row in estimates:
            model, term = row['model_id'], row['term']
            if model not in models or not term.strip():
                raise ValueError(f'unknown model or empty term: {(model, term)}')
            key = (model, term)
            if key in lookup:
                raise ValueError(f'duplicate estimate: {key}')
            label = row['label'].strip() or term
            if term in labels and labels[term] != label:
                raise ValueError(f'inconsistent label for {term}')
            if term not in terms:
                terms.append(term)
                labels[term] = label
            coefficient = number(row['coefficient'], 'coefficient')
            se = number(row['se'], 'se')
            p = number(row['p_value'], 'p_value')
            if se is not None and se < 0:
                raise ValueError(f'negative standard error: {key}')
            if p is not None and not 0 <= p <= 1:
                raise ValueError(f'p_value outside [0,1]: {key}')
            if coefficient is None and (p is not None or se is not None):
                raise ValueError(f'SE/p without coefficient: {key}')
            lookup[key] = (coefficient, se, p)
        header = [''] + [f'({i + 1}) {row["column_label"]}' for i, row in enumerate(meta)]
        rows = []
        for term in terms:
            coefficients, ses = [labels[term]], ['']
            for model in models:
                coefficient, se, p = lookup.get((model, term), (None, None, None))
                coefficients.append(EstimateCell(formatted(coefficient, args.digits), stars(p)))
                ses.append(f'({formatted(se, args.digits)})' if se is not None else '—')
            rows.extend([coefficients, ses])
        metadata_rows = [[field] + [(row.get(field) or '—') for row in meta]
                         for field in fields if field not in ('model_id', 'column_label')]
        note = args.note + ' Standard errors in parentheses when available. '
        note += '* p<0.10, ** p<0.05, *** p<0.01 (supplied p-values). '
        note += '—: unavailable or not applicable; distinguish in the substantive notes.'
        markdown = [f'### {md(args.title)}', '', '| ' + ' | '.join(map(md, header)) + ' |',
                    '|---|' + '---:|' * len(models)]
        markdown += ['| ' + ' | '.join(map(md, row)) + ' |' for row in rows + metadata_rows]
        markdown += ['', 'Notes: ' + md(note), '']
        latex = ['% Requires booktabs; use a Unicode-capable LaTeX setup for non-English labels.',
                 r'\begin{table}[htbp]', r'\centering', r'\caption{' + tex(args.title) + '}',
                 r'\begin{tabular}{l' + 'r' * len(models) + '}', r'\toprule',
                 ' & '.join(map(tex, header)) + r' \\', r'\midrule']
        latex += [' & '.join(map(tex, row)) + r' \\' for row in rows]
        latex += [r'\midrule']
        latex += [' & '.join(map(tex, row)) + r' \\' for row in metadata_rows]
        latex += [r'\bottomrule', r'\end{tabular}', r'\par\smallskip',
                  r'\parbox{\linewidth}{\footnotesize ' + tex(note) + '}', r'\end{table}', '']
        html_output = [
            '<!doctype html><html lang="zh-CN"><head><meta charset="utf-8">',
            '<meta name="viewport" content="width=device-width,initial-scale=1">',
            '<title>' + html.escape(args.title) + '</title>',
            '<style>body{font-family:"Times New Roman","Noto Serif CJK SC",serif;margin:32px;color:#111}',
            'table{border-collapse:collapse;min-width:600px;max-width:100%;font-variant-numeric:tabular-nums}',
            'caption{text-align:left;font-weight:bold;margin-bottom:16px}th,td{padding:7px 18px;text-align:right;white-space:nowrap}',
            'th:first-child,td:first-child{text-align:left}thead{border-top:2px solid #111;border-bottom:1px solid #111}',
            'tbody.parameters{border-bottom:1px solid #111}tbody.metadata{border-bottom:2px solid #111}',
            'tr.se td{padding-top:0;color:#222}sup{font-size:.72em;vertical-align:super;line-height:0}',
            '.notes{font-size:.9em;max-width:1000px;line-height:1.5}</style></head><body>',
            '<table><caption>' + html.escape(args.title) + '</caption><thead><tr>',
            ''.join('<th scope="col">' + html_cell(v) + '</th>' for v in header),
            '</tr></thead><tbody class="parameters">']
        for i, row in enumerate(rows):
            html_output.append('<tr' + (' class="se"' if i % 2 else '') + '>' +
                               ''.join('<td>' + html_cell(v) + '</td>' for v in row) + '</tr>')
        html_output.append('</tbody><tbody class="metadata">')
        html_output.extend('<tr>' + ''.join('<td>' + html_cell(v) + '</td>' for v in row) + '</tr>'
                           for row in metadata_rows)
        html_output.extend(['</tbody></table><p class="notes">Notes: ' + html.escape(note) + '</p>', '</body></html>'])
        output = Path(args.output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text('\n'.join(markdown), encoding='utf-8')
        output.with_suffix('.tex').write_text('\n'.join(latex), encoding='utf-8')
        output.with_suffix('.html').write_text('\n'.join(html_output), encoding='utf-8')
        print(f'Wrote {output}, {output.with_suffix(".tex")} and {output.with_suffix(".html")}')
    except (ValueError, OSError) as error:
        parser.error(str(error))


if __name__ == '__main__':
    main()
