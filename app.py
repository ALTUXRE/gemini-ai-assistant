from flask import Flask, render_template, request
from google import genai
import os

app = Flask(__name__)

# Replace with your actual Gemini API key or set as environment variable "GEMINI_API_KEY"
API_KEY = os.getenv("GEMINI_API_KEY", "Your api key here")

# Initialize Gemini client
client = genai.Client(api_key=API_KEY)

PROMPTS = {
    'answer': [
        "What is the capital of France?",
        "Explain the significance of the Eiffel Tower.",
        "Tell me three facts about Paris."
    ],
    'summarize': [
        "Summarize the following article:\n{text}",
        "What are the main points of this text?\n{text}",
        "Provide a brief overview of this document:\n{text}"
    ],
    'creative': [
        "Write a short story about a dragon and a princess.",
        "Create a poem about autumn.",
        "Generate an idea for a science fiction novel."
    ]
}

def get_gemini_response(prompt):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        return f"Error calling Gemini API: {e}"

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    feedback_given = False
    response_text = None
    show_feedback_form = False
    function = None
    prompt_style = None
    prompt_to_send = None

    if request.method == 'POST':
        # Handle feedback submission
        if 'feedback' in request.form:
            with open("feedback_log.txt", "a", encoding="utf-8") as f:
                f.write(f"Function: {request.form.get('fn')}\nPrompt: {request.form.get('prompt_for_feedback')}\nResponse: {request.form.get('response_for_feedback')}\nFeedback: {request.form.get('feedback')}\n{'-'*40}\n")
            feedback_given = True
            return render_template("index.html", feedback_given=feedback_given)

        function = request.form.get('function')
        prompt_style = request.form.get('prompt_style')
        custom_prompt = request.form.get('custom_prompt', '').strip()
        text_input = request.form.get('text_input', '').strip()

        if function not in PROMPTS:
            error = "Please select a function."
            return render_template("index.html", error=error)

        if prompt_style == "custom":
            if not custom_prompt:
                error = "Please enter a custom prompt."
                return render_template("index.html", error=error, function=function, prompt_style=prompt_style)
            prompt_to_send = custom_prompt
        else:
            try:
                idx = int(prompt_style) - 1
                prompt_template = PROMPTS[function][idx]
                if "{text}" in prompt_template:
                    if not text_input:
                        error = "Please enter text for this prompt."
                        return render_template("index.html", error=error, function=function, prompt_style=prompt_style)
                    prompt_to_send = prompt_template.replace("{text}", text_input)
                else:
                    prompt_to_send = prompt_template
            except Exception:
                error = "Invalid prompt style selected."
                return render_template("index.html", error=error, function=function, prompt_style=prompt_style)

        response_text = get_gemini_response(prompt_to_send)
        show_feedback_form = True

    return render_template("index.html",
                           function=function,
                           prompt_style=prompt_style,
                           prompt=prompt_to_send,
                           response=response_text,
                           error=error,
                           feedback_given=feedback_given,
                           show_feedback_form=show_feedback_form)

if __name__ == "__main__":
    app.run(debug=True)
