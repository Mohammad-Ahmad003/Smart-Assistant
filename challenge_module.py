import streamlit as st
import google.generativeai as genai
from utils.gemini_fallback import get_valid_response

# Load keys from Streamlit secrets
API_KEYS = st.secrets["GEMINI_KEYS"]

# Function to generate logical challenge questions
def generate_challenge_questions(document_text):
    prompt = f"""
You are a tutor AI. Read the following document and generate exactly 3 **logic-based** or **comprehension-focused** questions.

Each question should:
- Be relevant to document understanding.
- Encourage reasoning (not just factual recall).
- Be clearly numbered.

Document:
\"\"\"{document_text}\"\"\"

Give only the questions in this format:
1. ...
2. ...
3. ...
"""
    response_text = get_valid_response(prompt)
    return [line.strip() for line in response_text.split("\n") if line.strip().startswith(tuple("123"))]

# Function to evaluate the user's answers
def evaluate_answer(document_text, question, user_answer):
    prompt = f"""
You are an evaluator AI. A user is answering a question based on the following document.

Document:
\"\"\"{document_text}\"\"\"

Question:
{question}

User's Answer:
{user_answer}

Your task:
- Evaluate the user's response.
- Categorize it as ✅ Correct / ❌ Incorrect / 🤔 Partially correct.
- Provide **feedback in bullet points**.
- Give suggestions for improvement (if any).

Respond in this format:

**Evaluation**: ✅ / ❌ / 🤔

**Explanation**:

- ...
- ...
- ...

**Suggestions**:
- ...
- ...
"""
    return get_valid_response(prompt)
