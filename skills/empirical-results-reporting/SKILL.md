---
name: empirical-results-reporting
description: "Report econometric work in economics academic-paper form with standard regression tables, diagnostic and coefficient figures, specification records, economic interpretation, and identification limitations. Use whenever presenting regressions or empirical analyses, or converting Stata/R/Python outputs into research reports, baseline/robustness/IV/DID/RDD tables, event studies, or heterogeneity plots. 可独立用于计量结果汇报、经济学论文式回归表、统计图与研究报告，也可承接通用实证研究流程。"
---

# 经济学论文式计量汇报

## 工作边界

负责核验与组织已有计量结果、制作标准回归表和图、撰写本轮工作与结果报告。读取 `$empirical-research-protocol` 的交接材料（如有）；独立调用时核查用户提供的数据、日志、代码和输出。

按本轮实际分析范围汇报。缺失统计量先从可用估计对象或日志提取；补跑已授权的必要计算并记录。没有数据、授权或可用环境时标记缺失，不自行填数。

## 结果整理步骤

1. **清点**：列出本轮目的、所有已运行模型和失败模型、数据/样本、Y、D/X、估计器、控制变量、固定效应、推断、诊断与图形数据。区分新结果、此前结果及未经复核的用户摘录。
2. **核对**：将数字关联到 `run_id`、`spec_id`、参数名和原始结果定位；使用完整精度计算，不从四舍五入表格推导显著性。核查 p 值、标准误、区间采用同一推断口径。
3. **分组**：按经济学问题组织描述、基准、识别、稳健性、证伪、替代识别、机制、异质性和量级；仅将目标参数及单位可比较的估计并列表述。
4. **制表**：读取 [回归表规范](references/tables-and-results.md)，使用 [表格模板](assets/table_templates.md)。在对话中直接给出核心论文式表格；完整表格另存文件。默认系数一行、显著性星号在系数右上角，括号内标准误下一行且必须对齐同一模型列，每列一个明确设定。默认逐项展示全部可估计控制变量及其系数、标准误和星号，不能仅用“Controls: Yes/No”替代。
5. **制图**：读取 [图形规范](references/figures.md)，为适用分析绘制原始趋势、事件研究、RD、系数/稳健性/异质性图等。导出正式静态图与绘图数据，实际打开图检查坐标、标签、区间、裁切和可读性。
6. **解读**：对每张核心表写论文式段落，说明列间变化、首选结果、效应单位、估计不确定性、统计证据、经济量级、支持的结论及尚存问题。不得只说“显著/稳健”。
7. **报告**：按 [报告模板](assets/research_report.md) 生成 `research_report.md`；遵循 [报告与核验](references/report-and-checks.md)。短任务可在对话中给完整精简报告，不强制额外文档。

## 核心格式约定

- 默认中文正文，保留标准方法缩写；按用户要求使用英文。表题明确问题与因变量；列号配简洁设定标签，必要时多 panel。
- 报告真实标准误（括号）、N、分析单位数量、聚类层级及数量、控制/固定效应、估计器和样本信息；仅报告方法有定义且软件提供的拟合统计量。
- 默认三位小数；极小量改用合理精度或科学计数法，避免非零效应显示为 0.000。注明 `* p<0.10, ** p<0.05, *** p<0.01`，用实际推断 p 值生成右上角星号；使用调整 p 值时说明。主回归表默认不单列系数 p 值或置信区间，数值 p 和区间保留在完整结果文件中；识别诊断、联合检验、组间差异和弱IV等检验的 p 值仍按需要报告。p≥0.10时不加星，不得为了排版添加星号。
- “—”表示不适用或不可得，并在注释区分；空白单元格不代表零。不能估计的模型标注原因，不悄悄删除。
- 主表逐项列出全部可估计的实质性控制变量、变换/交互项和常数项（如实际估计），每项都给系数、同口径标准误与显著性星号。固定效应吸收项用设定行说明，不默认展开大量FE哑变量。仅在用户明确要求精简时省略控制系数，并提供完整附表。
- 控制变量不能从估计器直接获得时，明确区别“未加入”“被吸收/不可估计”和“估计器不提供共同斜率”。CSDID等主ATT表不捏造控制系数、不混入辅助FE回归或倾向得分/结果回归的nuisance参数；列出控制清单与调整方式，可获得的辅助估计另表呈现并标明其模型、因变量及非主效应性质。
- 表底逐项报告样本量、分析单位与聚类数量、固定效应、真实适用的R²/调整R²、模型F/Wald统计及检验p（可得且适用时）；不得只显示笼统“统计量”。方法不定义的统计量不硬填。
- Markdown用行内数学上标（例如 `$0.0016^{***}$`），HTML用`<sup>***</sup>`，LaTeX用`\textsuperscript{***}`；Word/PDF使用实际上标格式。不能仅把普通字号的`***`贴在系数右侧。
- 区分 OLS 系数、ATT/ATE/LATE、边际效应、弹性、比率及局部参数；不能直接比较的参数不得统一标成 Treatment effect 而不解释。
- 图默认展示 95% 置信区间，区分逐点/同时区间；使用估计器或合适推断导出的区间，不机械地设为系数±1.96SE。
- 对归一化指数、均值接近零/负值的 Y，优先用指数点或标准差解释，不机械计算效应/均值。线性、对数、二元和非线性模型使用各自正确量级转换。
- 明确诊断失败、统计功效有限、多重检验、样本变化、设定选择和不可比参数。联合前趋势检验不拒绝不能证明平行趋势；两组显著性不同不能证明异质性。

## 可复用制表脚本

将结构化估计存为 [estimates.csv](assets/estimates.csv)，设定信息存为 [model_metadata.csv](assets/model_metadata.csv)，再运行：

```bash
python <skill-dir>/scripts/render_regression_table.py \
  --estimates <estimates.csv> --metadata <model_metadata.csv> \
  --output <table.md> --title 'Table 2. Baseline estimates; dependent variable: Y' \
  --note '按真实推断填写标准误、样本、估计器与显著性口径。'
```

使用本 skill 实际路径替换 `<skill-dir>`。脚本输出 Markdown、同名 `.tex` 与 `.html`，按输入顺序排列模型和参数，保留缺失，所有输入参数（包括控制与常数）逐项输出，不估计模型、不推算 p 值；运行后检查上标渲染、完整控制清单和SE列对齐。Markdown查看器不支持行内数学时使用生成的HTML或适当文档格式，不能退化为同字号星号。复杂分 panel、诊断表或不同尺度结果按模板制作。

## 最终交付

在对话中至少给出：本轮完成了什么、核心回归表/适用诊断结果、论文式解读、结论和最需要处理的局限。附可用结果文件与图，不能只给日志或文件链接。

保留 `tables/`、`figures/`、绘图数据、完整估计与 `research_report.md` 的关联；沿用项目模型注册表，不另建冲突的编号体系。未执行模块只注明状态，不虚构结果，也不为凑齐报告额外运行所有方法。
