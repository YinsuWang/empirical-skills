#!/usr/bin/env python3
"""Install a local skill repository into the Codex user skill directory."""
import argparse
from datetime import datetime, timezone
from pathlib import Path
import shutil
import tempfile


def install(source, skill_root):
    source = source.resolve()
    manifest = source / 'SKILL.md'
    if not manifest.is_file():
        raise ValueError(f'SKILL.md missing: {source}')
    text = manifest.read_text(encoding='utf-8')
    name_line = next((line for line in text.splitlines() if line.startswith('name: ')), '')
    name = name_line.removeprefix('name: ').strip().strip('"\'')
    if name not in ('empirical-research-protocol', 'empirical-results-reporting'):
        raise ValueError('Unexpected skill name')
    skill_root = skill_root.expanduser().resolve()
    destination = skill_root / name
    if destination == source:
        raise ValueError('Source is already the installation destination')
    skill_root.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='empirical-skill-') as td:
        staged = Path(td) / name
        staged.mkdir()
        for item in ('SKILL.md', 'agents', 'references', 'assets', 'scripts'):
            p = source / item
            if p.is_dir():
                shutil.copytree(p, staged / item)
            elif p.is_file():
                shutil.copy2(p, staged / item)
        if destination.exists():
            stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
            backup = skill_root.parent / 'skill-backups' / f'{name}-{stamp}'
            backup.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(destination), str(backup))
            try:
                shutil.copytree(staged, destination)
            except Exception:
                if destination.exists():
                    shutil.rmtree(destination)
                shutil.move(str(backup), str(destination))
                raise
            print(f'Previous version backed up: {backup}')
        else:
            try:
                shutil.copytree(staged, destination)
            except Exception:
                if destination.exists():
                    shutil.rmtree(destination)
                raise
    print(f'Installed ${name}: {destination}')
    return destination


def install_both(checkout, skill_root):
    for name in ('empirical-research-protocol', 'empirical-results-reporting'):
        install(checkout / 'skills' / name, skill_root)


def main():
    import subprocess
    parser = argparse.ArgumentParser(description='Install both skills from YinsuWang/empirical-skills for local Codex.')
    parser.add_argument('--skill-root', type=Path, default=Path.home() / '.agents' / 'skills')
    parser.add_argument('--source-root', type=Path, help='Local empirical-skills checkout; defaults to the directory of this script if complete')
    args = parser.parse_args()
    local = args.source_root or Path(__file__).resolve().parent
    try:
        if args.source_root or all((local / 'skills' / n / 'SKILL.md').is_file() for n in ('empirical-research-protocol', 'empirical-results-reporting')):
            install_both(local, args.skill_root)
        else:
            if shutil.which('git') is None:
                raise ValueError('Install Git before running this installer')
            with tempfile.TemporaryDirectory(prefix='empirical-repository-') as td:
                checkout = Path(td) / 'empirical-skills'
                subprocess.run(['git', 'clone', '--depth', '1',
                                'https://github.com/YinsuWang/empirical-skills.git', str(checkout)], check=True)
                install_both(checkout, args.skill_root)
        print('Open Codex and check /skills. Restart Codex if the new skills are not visible.')
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        parser.exit(1, f'Installation failed: {error}\n')


if __name__ == '__main__':
    main()
