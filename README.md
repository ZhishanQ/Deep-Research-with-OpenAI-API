
# 🔬 Deep Research with OpenAI API

[中文文档](README_zh.md) | English

Build your own deep research tool powered by the OpenAI API. This Python script automates the research process: it first uses GPT-4o to interactively clarify your research question, then refines it into a comprehensive prompt, and finally executes the deep research to generate a detailed report.

## 🤷 Why Do We Need This Tool?

ChatGPT Plus subscription provides only **very limited deep research opportunities**. With this tool, you can:
- 🔥 Use the OpenAI API to perform **unlimited deep research** (pay-as-you-go)
- 💰 Have full control over your usage and costs
- 🛠️ Customize the research process to fit your specific needs

## ✨ Features

-   **🤔 Interactive Question Clarification**: Uses GPT-4o to ask clarifying questions to better understand your research needs.
-   **📝 Automated Prompt Engineering**: Synthesizes your original question and answers into a high-quality, detailed prompt for the research model.
-   **⚡ Dual Model Support**: Choose between a faster, lightweight model (`o4-mini-deep-research`) or a more comprehensive one (`o3-deep-research`).
-   **📊 Automatic Report Generation**: Calls the Deep Research API and saves the output as a timestamped Markdown file.

## 🚀 How to Use

### 1️⃣ Prerequisites

-   Python 3.x
-   An OpenAI API key.

### 2️⃣ Clone the Repository

```bash
git clone https://github.com/ZhishanQ/Deep-Research-with-OpenAI-API.git
cd Deep-Research-with-OpenAI-API
```

### 3️⃣ Install Dependencies

You need to install the following Python packages:

```bash
pip install openai
```

**📦 Required packages:**
- `openai` - The official OpenAI Python client library (the newest version is recommended)

⚠️ If your code reports errors, please upgrade `openai` to newest version by:

```bash
pip install --upgrade openai
```

### 4️⃣ Set Up Your API Key

You need to set your OpenAI API key as an environment variable.

**🍎 On macOS/Linux:**

```bash
export OPENAI_API_KEY='your-api-key-here'
```

**🪟 On Windows:**

```bash
set OPENAI_API_KEY=your-api-key-here
```

> **💡 Note:** Replace `'your-api-key-here'` with your actual OpenAI API key.

<details>
<summary><strong>📌 Permanently add to shell profile (Optional) - Click to expand</strong></summary>

<br>

Or permanently add it to your shell profile (e.g., `~/.bashrc`, `~/.zshrc`) by:

🐧 Linux:

```bash 
echo "export OPENAI_API_KEY='your-api-key-here'" >> ~/.bashrc
source ~/.bashrc
```

🍎 MacOS:

```bash 
echo "export OPENAI_API_KEY='your-api-key-here'" >> ~/.zshrc
source ~/.zshrc
```

</details>

<details>
<summary><strong>🌐 Using a Custom API URL (Optional) - Click to expand</strong></summary>

<br>

If you're using a third-party API provider instead of the official OpenAI API, you need to customize the API base URL.

**Method 1: Set via environment variable**

```bash
export OPENAI_BASE_URL='https://your-custom-api-url.com/v1'
```

**Method 2: Modify the code directly**

Open `main_en.py` or `main_zh.py` and modify the client initialization section:

```python
# Find this section at the beginning of the file
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://your-custom-api-url.com/v1",  # Add this line
    timeout=3600
)
```

> **💡 Note:** Replace `https://your-custom-api-url.com/v1` with your actual API endpoint URL.

</details>

### 5️⃣ Configure the Script

Open `main_en.py` (for English interface) or `main_zh.py` (for Chinese interface) in a text editor. Find the following line and replace the placeholder text with your research topic:

```python
original_question = r"""your research question goes here"""
```

### 6️⃣ Run the Script

Execute the script from your terminal:

```bash
# For the English version
python main_en.py

# For the Chinese version
python main_zh.py
```

The script will guide you through the process of clarifying your question and then perform the research. The final report will be saved as a `.md` file in the same directory.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

