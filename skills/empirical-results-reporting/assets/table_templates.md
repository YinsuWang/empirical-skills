# 论文式表格模板

所有占位符都需替换为真实结果；未执行或不可得时明确标记。模板不含实证结果。

## Summary statistics

| Variable | Mean | SD | Min | Max | N |
|---|---:|---:|---:|---:|---:|
| [Y] | | | | | |
| [D/X] | | | | | |

注明样本、单位、权重、构造与缺失规则。处理前组间比较可加treated/control均值、标准化差异与适用差异检验。

## Baseline regression

| Dependent variable: [Y] | (1) [原样本] | (2) [共同样本] | (3) [首选] |
|---|---:|---:|---:|
| [Treatment/核心变量] | [beta] | [beta] | [beta] |
| | ([SE]) | ([SE]) | ([SE]) |
| Controls | No | No | Yes |
| Unit FE | [实际] | [实际] | [实际] |
| Time FE | [实际] | [实际] | [实际] |
| Estimator / estimand | | | |
| Sample | | | |
| Mean dependent variable | | | |
| Observations | | | |
| Units | | | |
| Cluster level / number | | | |
| [适用R²类型] | | | |

Notes: 填写变量单位、完整设定、权重、推断、聚类数量、SE口径、星号定义和省略控制变量。实际任务不需要的列/行可移除。

## IV evidence

| | (1) [Spec] | (2) [Spec] |
|---|---:|---:|
| **Panel A. OLS; outcome: [Y]** | | |
| [X] | [beta] | [beta] |
| | ([SE]) | ([SE]) |
| **Panel B. Reduced form; outcome: [Y]** | | |
| [Z] | [gamma] | [gamma] |
| | ([SE]) | ([SE]) |
| **Panel C. 2SLS; outcome: [Y]** | | |
| [X] | [beta_IV] | [beta_IV] |
| | ([SE]) | ([SE]) |
| **Panel D. First stage; outcome: [X]** | | |
| [Z] | [pi] | [pi] |
| | ([SE]) | ([SE]) |
| [适用强度/秩统计名称] | | |
| [弱IV稳健检验/区间] | | |
| Controls / FE / sample / inference | | |
| Observations / clusters | | |

工具和内生变量不止一个时展开，诊断归属于实际第一阶段；可比性不足时分表。

## Identification diagnostics

| Spec ID | Assumption / threat | Diagnostic | Sample / support | Statistic / CI | p-value | Interpretation |
|---|---|---|---|---|---|---|

## Robustness / falsification

| Spec ID | Threat | Test / changed specification | Estimand | Estimate | SE / CI | N | Interpretation |
|---|---|---|---|---:|---|---:|---|

正式回归附表仍用系数/SE两行结构；此表用于检验目的概览。

## Mechanisms and heterogeneity

| Dependent variable / group | (1) [M1] | (2) [M2] | (3) [Y/group] |
|---|---:|---:|---:|
| [D/主参数] | | | |
| | ([SE]) | ([SE]) | ([SE]) |
| Estimator / controls / FE | | | |
| Observations / support | | | |
| [组间差异及适用p] | | | |

注明D→M证据/因果中介的区别、分组时间、差异检验方法、多重检验和参数可比性。

## Economic magnitude

| Spec ID | Original estimate / CI | Transformation | Reference statistic / source | Magnitude / CI | Assumptions |
|---|---|---|---|---|---|
