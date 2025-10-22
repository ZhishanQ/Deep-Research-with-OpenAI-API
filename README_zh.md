# 🔬 使用 OpenAI API 进行深度研究

中文文档 | [English](README.md)

一个强大的 Python 脚本，利用 OpenAI API 自动化深度研究流程。它首先通过 GPT-4o 交互式地澄清您的研究问题，然后将其优化为一个高质量的提示，最终执行深度研究并生成一个综合性的研究报告。

## 🤷 为什么我们需要这个工具？

ChatGPT Plus 订阅仅提供**非常有限的深度搜索机会**。使用这个工具，您可以：
- 🔥 通过 OpenAI API 进行**无限次深度研究**（按使用量付费）
- 💰 完全掌控您的使用情况和成本
- 🛠️ 根据您的特定需求自定义研究流程

## ✨ 功能特性

-   **🤔 交互式问题澄清**: 使用 GPT-4o 提出澄清性问题，以更准确地理解您的研究需求。
-   **📝 自动化提示工程**: 将您的原始问题和补充回答整合成一个高质量、详细的研究提示。
-   **⚡ 双模型支持**: 可选择速度更快的轻量级模型 (`o4-mini-deep-research`) 或更全面的深度模型 (`o3-deep-research`)。
-   **📊 自动化报告生成**: 调用深度研究 API，并将结果保存为带时间戳的 Markdown 文件。

## 🚀 如何使用

### 1️⃣ 环境要求

-   Python 3.x
-   一个 OpenAI API 密钥。

### 2️⃣ 克隆仓库

```bash
git clone https://github.com/ZhishanQ/Deep-Research-with-OpenAI-API.git
cd Deep-Research-with-OpenAI-API
```

### 3️⃣ 安装依赖

您需要安装以下 Python 包：

```bash
pip install openai
```

**📦 必需的包:**
- `openai` - OpenAI 官方 Python 客户端库（建议使用最新版本）

⚠️ 如果代码报错，请升级 `openai` 到最新版本：

```bash
pip install --upgrade openai
```

### 4️⃣ 设置 API 密钥

您需要将您的 OpenAI API 密钥设置为环境变量。

**🍎 在 macOS/Linux 上:**

```bash
export OPENAI_API_KEY='你的-API-密钥'
```


**🪟 在 Windows 上:**

```bash
set OPENAI_API_KEY=你的-API-密钥
```

> **💡 注意:** 请将 `'你的-API-密钥'` 替换为您真实的 OpenAI API 密钥。

<details>
<summary><strong>📌 永久添加到 shell 配置文件（可选）- 点击展开</strong></summary>

<br>

或者永久添加到您的 shell 配置文件中（例如 `~/.bashrc`、`~/.zshrc`）：

🐧 Linux:

```bash 
echo "export OPENAI_API_KEY='你的-API-密钥'" >> ~/.bashrc
source ~/.bashrc
```

🍎 MacOS:

```bash 
echo "export OPENAI_API_KEY='你的-API-密钥'" >> ~/.zshrc
source ~/.zshrc
```

</details>

<details>
<summary><strong>🌐 使用自定义 API URL（可选）- 点击展开</strong></summary>

<br>

如果您使用的不是 OpenAI 官方 API，而是第三方 API 提供商，您需要自定义 API 地址。

**方法 1: 通过环境变量设置**

```bash
export OPENAI_BASE_URL='https://your-custom-api-url.com/v1'
```

**方法 2: 直接修改代码**

打开 `main_zh.py` 或 `main_en.py`，修改客户端初始化部分：

```python
# 在文件开头找到这部分代码
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://your-custom-api-url.com/v1",  # 添加这一行
    timeout=3600
)
```

> **💡 注意:** 请将 `https://your-custom-api-url.com/v1` 替换为您实际的 API 端点地址。

</details>

### 5️⃣ 配置脚本

在文本编辑器中打开 `main_zh.py` (中文版) 或 `main_en.py` (英文版)。找到下面这行代码，并将占位符文本替换为您自己的研究问题：

```python
original_question = r"""your research question goes here"""
```

### 6️⃣ 运行脚本

在您的终端中执行脚本：

```bash
# 运行中文版
python main_zh.py

# 运行英文版
python main_en.py
```

脚本将引导您完成问题澄清的步骤，然后开始进行研究。最终的研究报告将以 `.md` 文件的形式保存在同一个目录下。

## 📄 许可证

该项目基于 MIT 许可证。详情请参阅 [LICENSE](LICENSE) 文件。
