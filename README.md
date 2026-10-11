# Empirical Skills for Codex

两套可独立或配合调用的实证研究 skills，支持 Stata、R、Python 等分析环境。

| Skill | 用途 |
|---|---|
| `empirical-research-protocol` | 研究设计、数据审查、变量构造、识别、估计、诊断、稳健性、机制、异质性、经济解释与可复现记录 |
| `empirical-results-reporting` | 标准经济学回归表、典型诊断图、论文式结果解读、经济量级和识别局限；附 Markdown/LaTeX 制表工具 |

## Windows 安装

需要 Python 3.9+；使用 git clone 时需要 Git。在 PowerShell 执行：

```powershell
git clone https://github.com/YinsuWang/empirical-skills.git
py -3 .\empirical-skills\install.py
```

没有 `py` 但有 Python 时，将 `py -3` 换成 `python`。也可从 GitHub 下载 ZIP、解压后，在解压目录运行 `py -3 .\install.py`。

脚本默认将两套完整技能安装到 `%USERPROFILE%\.agents\skills\`，已有同名技能会备份到 `%USERPROFILE%\.agents\skill-backups\`。只安装技能自身的文件，不复制 README 或安装器。

## macOS / Linux 安装

```bash
git clone https://github.com/YinsuWang/empirical-skills.git
python3 ./empirical-skills/install.py
```

默认用户技能目录是 `~/.agents/skills/`。官方文档：[Build skills](https://learn.chatgpt.com/docs/build-skills)。需要旧目录的 Codex 版本可显式指定安装位置，例如 Windows：

```powershell
py -3 .\empirical-skills\install.py --skill-root "$env:USERPROFILE\.codex\skills"
```

选择你的 Codex 实际发现的目录，避免在多个发现位置重复安装同名技能。自定义路径不会自动修改 Codex 配置。

## 使用

打开 Codex，用 `/skills` 检查，或在请求中显式调用：

```text
使用 $empirical-research-protocol 完成本轮实证分析，明确每一步的目的、操作、产出与判断标准。

使用 $empirical-results-reporting 汇报本轮计量结果，展示标准回归表、适用图形、经济量级与识别局限。

同时使用 $empirical-research-protocol 和 $empirical-results-reporting，完成这一轮分析并按经济学论文形式汇报。
```

若安装后没有显示，重启 Codex。两套 skill 可以由适合其描述的任务自动触发；实际是否采用由 Codex 和当前配置决定。

也可以让本地 Codex 的 `$skill-installer` 从本仓库分别安装 `skills/empirical-research-protocol` 和 `skills/empirical-results-reporting`。

## 更新

```powershell
git -C .\empirical-skills pull --ff-only
py -3 .\empirical-skills\install.py
```

## 内容与边界

研究框架按任务范围选取步骤，覆盖 FE、DID、连续处理、IV、RDD、实验、匹配、合成控制、ITS、空间、非线性/动态/结构估计等方法。结果汇报 skill 包含回归表、图形、报告模板和可复用制表脚本。

保留全部主要设定及失败结果，区分探索与独立验证，识别诊断不支持假设时如实说明。仓库不包含任何研究数据或实证结果，也不自带 Stata/R 等统计软件。Python 制表工具只格式化已核验估计，不执行回归或补造统计量。

安装说明按 2026-10-11 核查的官方文档编写。Python 安装器已验证首次安装、重复安装备份及缺失 manifest 的错误处理；安装到你的电脑后，请在 Codex `/skills` 中确认。
