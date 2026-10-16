# 论文式表格模板

所有占位符都需替换为真实结果；未执行或不可得时明确标记。模板不含实证结果。

## Summary statistics

| Variable | Mean | SD | Min | Max | N |
|---|---:|---:|---:|---:|---:|
| [Y] | | | | | |
| [D/X] | | | | | |

注明样本、单位、权重、构造与缺失规则。处理前组间比较可加treated/control均值、标准化差异与适用差异检验。

## Baseline regression

适用时分为无控制／有控制两个panel，每个panel按无固定效应、仅时间、仅个体、双向固定效应排列四列，全部使用同一共同样本。以下为参数与统计行示例，按实际适用组合扩列，逐列填写控制、Unit FE和Time FE；CSDID等方法按实际估计结构展示，不能机械套用八列。

**Panel [A：无控制／B：有控制]**（分别使用下表；无控制panel的控制项填“—”）

| Dependent variable: [Y] | (1) 无固定效应 | (2) 仅时间FE | (3) 仅个体FE | (4) 双向FE |
|---|---:|---:|---:|---:|
| [Treatment/核心变量] | $[beta]^{[stars]}$ | $[beta]^{[stars]}$ | $[beta]^{[stars]}$ | $[beta]^{[stars]}$ |
| | ([SE]) | ([SE]) | ([SE]) | ([SE]) |
| [控制变量 X1] | [实际值] | [实际值] | $[beta_X1]^{[stars]}$ | $[beta_X1]^{[stars]}$ |
| | [实际值] | [实际值] | ([SE_X1]) | ([SE_X1]) |
| [控制变量 X2／变换／交互项] | [实际值] | [实际值] | $[beta_X2]^{[stars]}$ | $[beta_X2]^{[stars]}$ |
| | [实际值] | [实际值] | ([SE_X2]) | ([SE_X2]) |
| [其余全部控制变量，逐项展开] | [实际值] | [实际值] | [逐项系数及上标星号] | [逐项系数及上标星号] |
| | [实际值] | [实际值] | ([对应SE]) | ([对应SE]) |
| 常数项（如估计） | $[constant]^{[stars]}$ | $[constant]^{[stars]}$ | $[constant]^{[stars]}$ | $[constant]^{[stars]}$ |
| | ([SE]) | ([SE]) | ([SE]) | ([SE]) |
| Unit FE | No | No | Yes | Yes |
| Time FE | No | Yes | No | Yes |
| Estimator / estimand | | | | |
| Sample | | | | |
| Mean dependent variable | | | | |
| Observations | | | | |
| Units | | | | |
| Cluster level / number | | | | |
| [适用R²类型] | | | | |
| 调整R²（适用时） | | | | |
| [F/Wald等适用模型检验统计量] | | | | |
| [模型检验p值，适用时] | | | | |

Notes: 填写变量单位、完整设定、权重、推断、聚类数量、SE口径、星号定义。星号必须在系数右上角，SE必须对齐同列；所有可估计控制逐项输出，不能以Controls=Yes替代。[stars]按实际p替换为*、**、***或无上标。默认不单列系数p或CI。CSDID等无共同控制斜率的方法只展示真实主参数，列出控制清单与调整方式并标明状态，辅助参数另表注明性质。实际不适用的统计行可移除。

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

每个panel都展开其可估计控制变量与常数项的系数、同列SE及上标星号；使用实际该panel样本和统计量。工具和内生变量不止一个时展开，诊断归属于实际第一阶段；可比性不足时分表。

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

展开全部可估计控制/常数及其上标星号和SE，不只标controls=Yes；注明D→M证据/因果中介的区别、分组时间、差异检验方法、多重检验和参数可比性。

## Economic magnitude

| Spec ID | Original estimate / CI | Transformation | Reference statistic / source | Magnitude / CI | Assumptions |
|---|---|---|---|---|---|
