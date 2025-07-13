# 🧠 Smart Assistant for Research Summarization

A modular AI-powered assistant that reads PDF or TXT documents, generates summaries, answers questions, and challenges users with logical reasoning tasks.

## 🖥️ Setup Instructions

1. Clone the repository or unzip the downloaded file.
2. Open Command Prompt and navigate into the folder.
3. Create and activate a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```
4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Add your OpenAI API key to `.streamlit/secrets.toml`:
   ```toml
   [secrets]
   OPENAI_API_KEY = "your-key-here"
   ```
6. Run the app:
   ```
   streamlit run app.py
   ```

## ✅ Features

- Upload and analyze PDF or TXT files
- Auto summarize in ≤150 words
- Ask Anything Q&A with justification
- “Challenge Me” mode with 3 questions + feedback
