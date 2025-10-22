import os
from openai import OpenAI
from datetime import datetime

# 初始化 OpenAI 客户端 (设置 1 小时超时)
# 如果您使用的是第三方 API 提供商，可以设置自定义的 base URL：
# 方法 1: 通过环境变量设置: export OPENAI_BASE_URL='https://your-custom-api-url.com/v1'
# 方法 2: 在下方添加 base_url 参数：
#   client = OpenAI(
#       api_key=os.getenv("OPENAI_API_KEY"),
#       base_url="https://your-custom-api-url.com/v1",  # 取消注释并修改这一行
#       timeout=3600
#   )
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    timeout=3600  # 3600秒 = 1小时
)

# 定义研究问题
original_question = r"""your research question goes here"""

# 检查研究问题是否已被修改
if original_question.strip() == "your research question goes here" or not original_question.strip():
    print("=" * 60)
    print("❌ 请先在代码中填写您的研究问题 (original_question) 后再运行本程序。")
    print("请将 'your research question goes here' 替换为您的实际研究问题。")
    print("=" * 60)
    exit(1)


# --- 功能 1: 让用户选择是否澄清问题 ---
print("=" * 60)
print("🔍 OpenAI Deep Research 工具")
print("=" * 60)
print(f"原始研究问题: {original_question}\n")

while True:
    clarify_choice = input("是否需要通过提问来澄清和优化您的问题以获得更好的结果? (y/n): ").strip().lower()
    if clarify_choice in ['y', 'n']:
        break
    else:
        print("❌ 无效输入,请输入 'y' 或 'n'")

final_prompt = original_question

if clarify_choice == 'y':
    while True:
        try:
            # --- 步骤 1: 澄清问题 ---
            print("\n" + "=" * 60)
            print("🔍 步骤 1: 澄清问题")
            print("=" * 60)
            print("🤖 正在使用 gpt-4o 生成澄清问题,请稍候...")

            clarification_instructions = """
            You are talking to a user who is asking for a research task to be conducted. Your job is to gather more information from the user to successfully complete the task.
            GUIDELINES:
            - Be concise while gathering all necessary information.
            - Make sure to gather all the information needed to carry out the research task in a concise, well-structured manner.
            - Use bullet points or numbered lists if appropriate for clarity.
            - Don't ask for unnecessary information, or information that the user has already provided.
            IMPORTANT: Do NOT conduct any research yourself, just gather information that will be given to a researcher to conduct the research task.
            """
            clarification_response = client.chat.completions.create(
              model="gpt-4o",
              messages=[
                  {"role": "system", "content": clarification_instructions},
                  {"role": "user", "content": original_question}
              ]
            )
            clarifying_questions = clarification_response.choices[0].message.content

            print("\n🤔 为了更好地理解您的需求,请回答以下问题:\n")
            print(clarifying_questions)
            print("-" * 60)

            print("请输入您的补充信息 (输入完成后,按两次 Enter 结束):")
            user_answers = []
            while True:
                line = input()
                if not line:
                    break
                user_answers.append(line)
            answers_text = "\n".join(user_answers)

            # --- 步骤 2: 提示重写 ---
            print("\n" + "=" * 60)
            print("📝 步骤 2: 重写提示")
            print("=" * 60)
            print("🤖 正在使用 gpt-4o 整合信息并优化研究提示,请稍候...")

            prompt_rewriting_instructions = f"""
            You are an expert in crafting high-quality, detailed research prompts.
            Your task is to take the user's original query and their answers to clarifying questions, and rewrite them into a single, comprehensive, and well-structured prompt for a deep research model.
            GUIDELINES:
            - Synthesize the original question and the user's clarifications into a coherent whole.
            - Structure the prompt logically. Start with the core research goal, then add constraints, desired output formats, and other specific details.
            - Be explicit about what the user wants. Fill in any logical gaps based on the provided context.
            - The final output should be ONLY the rewritten prompt, without any extra text or explanation.
            Original Question:
            {original_question}
            User's Answers to Clarifying Questions:
            {answers_text}
            """
            rewritten_prompt_response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are an expert prompt engineer."},
                    {"role": "user", "content": prompt_rewriting_instructions}
                ]
            )
            final_prompt = rewritten_prompt_response.choices[0].message.content
            print("\n✅ 提示重写完成!")

            # --- 功能 2: 展示最终提交的问题并获取用户反馈 ---
            print("\n" + "=" * 60)
            print("✨ 这是为您优化后的最终研究提示:")
            print("=" * 60)
            print(final_prompt)
            print("-" * 60)
            
            feedback = input("按 Enter 键继续研究, 或输入 'r' 重新澄清问题: ").strip().lower()
            if feedback == 'r':
                print("\n🔄 好的,让我们再试一次...")
                continue  # 重新开始澄清循环
            else:
                break  # 满意,跳出循环

        except Exception as e:
            print(f"\n❌ 在澄清或重写步骤中发生错误: {e}")
            print("🤔 将使用原始问题进行研究。")
            final_prompt = original_question
            break # 发生错误,跳出循环
else:
    print("\n✅ 好的,将直接使用原始问题进行研究。")


# --- 最后一步: 用户选择模型并执行深度研究 ---
print("\n" + "=" * 60)
print("🚀 最后一步: 选择深度研究模型并执行")
print("=" * 60)
print("\n请选择模型:")
print("  [1] o4-mini-deep-research (轻量版 - 更快速)")
print("  [2] o3-deep-research (完整版 - 更深度)")
print("-" * 60)

while True:
    choice = input("请输入选项 (1 或 2): ").strip()
    if choice == "1":
        model_name = "o4-mini-deep-research"
        model_label = "o4-mini (轻量版)"
        break
    elif choice == "2":
        model_name = "o3-deep-research"
        model_label = "o3 (完整版)"
        break
    else:
        print("❌ 无效选项,请输入 1 或 2")

print(f"\n✅ 已选择: {model_label}")
print("🔄 正在进行深度研究,请稍候...")
print("⏳ 这可能需要几分钟时间,模型正在搜索网络和分析数据...\n")

# 调用 Deep Research API
try:
    response = client.responses.create(
        model=model_name,
        input=[
            {"role": "user", "content": [{"type": "input_text", "text": final_prompt}]}
        ],
        reasoning={"summary": "auto"},
        tools=[
            {"type": "web_search_preview"},
            {"type": "code_interpreter", "container": {"type": "auto"}}
        ]
    )
    # 获取最终报告内容
    report_content = response.output_text
except Exception as e:
    print(f"❌ 调用 Deep Research API 时出错: {e}")
    report_content = f"研究失败: {e}"


# 生成文件名(带时间戳)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"deep_research_report_{timestamp}.md"

# 保存为 Markdown 文件
with open(filename, "w", encoding="utf-8") as f:
    f.write(report_content)

print(f"✅ 研究报告已保存至: {filename}")
print(f"📄 文件大小: {len(report_content)} 字符")
print("\n" + "="*50)
print("报告预览:")
print("="*50)
print(report_content[:500] + "..." if len(report_content) > 500 else report_content)
