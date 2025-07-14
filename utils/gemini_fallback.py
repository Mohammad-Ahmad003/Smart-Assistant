# utils/gemini_fallback.py
import streamlit as st
import google.generativeai as genai

API_KEYS = st.secrets["GEMINI_KEYS"]

if "working_key" not in st.session_state:
    st.session_state.working_key = None
if "working_key" not in st.session_state:
    st.session_state.working_key = None
if "failed_keys" not in st.session_state:
    st.session_state.failed_keys = set()

def get_valid_response(prompt):
    keys_to_try = [st.session_state.working_key] if st.session_state.working_key else []
    keys_to_try += [k for k in API_KEYS if k != st.session_state.working_key and k not in st.session_state.failed_keys]

    for key in keys_to_try:
        try:
            genai.configure(api_key=key)
            model = genai.GenerativeModel("models/gemini-1.5-flash-latest")
            response = model.generate_content(prompt)
            st.session_state.working_key = key
            return response.text.strip()
        except Exception as e:
            if "quota" in str(e).lower() or "resourceexhausted" in str(e).lower():
                st.session_state.failed_keys.add(key)
            continue
    return "❌ All API keys failed or quota exceeded. Please try again later."
