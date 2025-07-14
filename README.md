
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
📫 API Testing with Postman
You can test the Smart Assistant APIs using the provided Postman collection.
-> Download Collection
File: postman/SmartAssistant.postman_collection.json

-> How to Use
Open Postman.

Go to File > Import.

Select the JSON file.

Start testing the APIs locally or with the hosted Streamlit backend.
## ✅ Features

- Upload and analyze PDF or TXT files
- Auto summarize in ≤150 words
- Ask Anything Q&A with justification
- “Challenge Me” mode with 3 questions + feedback

## 📎 Project Links
- 🔗 Live App: [Smart Assistant](https://kn4qmtsxy8jfgsuceeda4p.streamlit.app/)
- 📂 GitHub Repo: [Smart Assistant on GitHub](https://github.com/Mohammad-Ahmad003/Smart-Assistant)

