# Gemini AI Assistant (Flask Web App)

A web-based AI assistant built with Flask and powered by Google's Gemini API.  
Users can ask questions, get text summaries, or generate creative content via preset or custom prompts.  
Includes a feedback mechanism to collect user inputs for continuous prompt improvement.

## Features

- Select between **Answering factual questions**, **Text summarization**, and **Creative content generation**
- Choose from multiple prompt styles or enter custom prompts
- Dynamic text input support for prompts requiring additional text
- Integration with Google Gemini API (free tier)
- Feedback collection and saving in a local log file (`feedback_log.txt`)

## Project Structure

gemini-flask-ai-assistant/
├── app.py # Flask server code
├── requirements.txt # Required Python packages
├── feedback_log.txt # Stores user feedback (created after first use)
└── templates/
└── index.html # HTML template for the UI

text

## Setup and Run Locally

1. Clone this repository:

git clone https://github.com/yourusername/gemini-ai-assistant.git
cd gemini-ai-assistant

text

2. (Recommended) Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate # Linux/macOS
venv\Scripts\activate # Windows

text

3. Install dependencies:

pip install -r requirements.txt

text

4. Set your Gemini API key as an environment variable:

export GEMINI_API_KEY="your_gemini_api_key" # Linux/macOS
set GEMINI_API_KEY=your_gemini_api_key # Windows (cmd)

text

5. Run the Flask app:

python app.py

text

6. Open your browser and visit:

http://127.0.0.1:5000/

text

## Usage

- Select a function and prompt style or enter a custom prompt.
- Provide text if required by the prompt.
- Submit to get AI-generated response.
- Provide feedback (Yes/No) to help improve the assistant.

## Notes

- This app uses Google Gemini API free tier; ensure your API key is active and has quota.
- Feedback is stored locally; review `feedback_log.txt` for user input analytics.
- This project is ideal for learning prompt engineering and building AI assistants with modern APIs.

Happy coding! Feel free to contribute or report issues.

