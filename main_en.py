import os
from openai import OpenAI
from datetime import datetime

# Initialize the OpenAI client (with a 1-hour timeout)
# If you're using a third-party API provider, you can set a custom base URL:
# Method 1: Set via environment variable: export OPENAI_BASE_URL='https://your-custom-api-url.com/v1'
# Method 2: Add base_url parameter below:
#   client = OpenAI(
#       api_key=os.getenv("OPENAI_API_KEY"),
#       base_url="https://your-custom-api-url.com/v1",  # Uncomment and modify this line
#       timeout=3600
#   )
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    timeout=3600  # 3600 seconds = 1 hour
)

# Define the research question
original_question = r"""your research question goes here"""
# original_question = r"""please introduce the development history of open source software."""


# --- Ensure the research question is set ---
if original_question.strip().lower() == "your research question goes here" or not original_question.strip():
    print("=" * 60)
    print("❌ ERROR: Please replace the placeholder with your actual research question in the script.")
    print("=" * 60)
    exit(1)


# --- Feature 1: Let the user choose whether to clarify the question ---
print("=" * 60)
print("🔍 OpenAI Deep Research Tool")
print("=" * 60)
print(f"Original research question: {original_question}\n")

while True:
    clarify_choice = input("Do you want to clarify and optimize your question for better results? (y/n): ").strip().lower()
    if clarify_choice in ['y', 'n']:
        break
    else:
        print("❌ Invalid input, please enter 'y' or 'n'")

final_prompt = original_question

if clarify_choice == 'y':
    while True:
        try:
            # --- Step 1: Clarifying the Question ---
            print("\n" + "=" * 60)
            print("🔍 Step 1: Clarifying the Question")
            print("=" * 60)
            print("🤖 Generating clarifying questions using gpt-4o, please wait...")

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

            print("\n🤔 To better understand your needs, please answer the following questions:\n")
            print(clarifying_questions)
            print("-" * 60)

            print("Please enter your additional information (press Enter twice to finish):")
            user_answers = []
            while True:
                line = input()
                if not line:
                    break
                user_answers.append(line)
            answers_text = "\n".join(user_answers)

            # --- Step 2: Rewriting the Prompt ---
            print("\n" + "=" * 60)
            print("📝 Step 2: Rewriting the Prompt")
            print("=" * 60)
            print("🤖 Consolidating information and optimizing the research prompt using gpt-4o, please wait...")

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
            print("\n✅ Prompt rewriting complete!")

            # --- Feature 2: Display the final submitted question and get user feedback ---
            print("\n" + "=" * 60)
            print("✨ Here is the optimized final research prompt for you:")
            print("=" * 60)
            print(final_prompt)
            print("-" * 60)
            
            feedback = input("Press Enter to continue with the research, or type 'r' to clarify the question again: ").strip().lower()
            if feedback == 'r':
                print("\n🔄 Okay, let's try again...")
                continue  # Restart the clarification loop
            else:
                break  # Satisfied, exit the loop

        except Exception as e:
            print(f"\n❌ An error occurred during the clarification or rewriting step: {e}")
            print("🤔 Will proceed with the original question for the research.")
            final_prompt = original_question
            break # Error occurred, exit the loop
else:
    print("\n✅ Okay, proceeding directly with the original question for the research.")


# --- Final Step: Select a Deep Research Model and Execute ---
print("\n" + "=" * 60)
print("🚀 Final Step: Select a Deep Research Model and Execute")
print("=" * 60)
print("\nPlease select a model:")
print("  [1] o4-mini-deep-research (Lightweight - Faster)")
print("  [2] o3-deep-research (Full version - More in-depth)")
print("-" * 60)

while True:
    choice = input("Please enter your choice (1 or 2): ").strip()
    if choice == "1":
        model_name = "o4-mini-deep-research"
        model_label = "o4-mini (Lightweight)"
        break
    elif choice == "2":
        model_name = "o3-deep-research"
        model_label = "o3 (Full version)"
        break
    else:
        print("❌ Invalid choice, please enter 1 or 2")

print(f"\n✅ Selected: {model_label}")
print("🔄 Conducting deep research, please wait...")
print("⏳ This may take a few minutes as the model is searching the web and analyzing data...\n")

# Call the Deep Research API
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
    # Get the final report content
    report_content = response.output_text
except Exception as e:
    print(f"❌ Error calling Deep Research API: {e}")
    report_content = f"Research failed: {e}"


# Generate a filename with a timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"deep_research_report_{timestamp}.md"

# Save as a Markdown file
with open(filename, "w", encoding="utf-8") as f:
    f.write(report_content)

print(f"✅ Research report saved to: {filename}")
print(f"📄 File size: {len(report_content)} characters")
print("\n" + "="*50)
print("Report Preview:")
print("="*50)
print(report_content[:500] + "..." if len(report_content) > 500 else report_content)
