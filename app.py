import streamlit as st
from summarizer import generate_summary
from qa_module import answer_question
from challenge_module import generate_challenge_questions, evaluate_answer
import PyPDF2

# --------------------
# ⚙️ Session State Init
# --------------------
if "document_text" not in st.session_state:
    st.session_state.document_text = ""

if "qa_memory" not in st.session_state:
    st.session_state.qa_memory = []

if "challenge_questions" not in st.session_state:
    st.session_state.challenge_questions = []

if "qa_history" not in st.session_state:
    st.session_state.qa_history = []

# -------------------
# 📄 File Extraction
# -------------------
def extract_text(file):
    if file.type == "application/pdf":
        reader = PyPDF2.PdfReader(file)
        return "\n".join([page.extract_text() or "" for page in reader.pages])
    elif file.type == "text/plain":
        return file.read().decode("utf-8")
    return ""

# -------------------
# 🎨 UI Configuration
# -------------------
st.set_page_config(page_title="📄 Smart Assistant", layout="wide")
st.title("📄 Smart Assistant for Research Summarization")

# -------------------
# 📁 Sidebar Upload
# -------------------
with st.sidebar:
    st.header("📤 Upload Document")
    uploaded_file = st.file_uploader("PDF or TXT", type=["pdf", "txt"])
    if uploaded_file:
        st.session_state.document_text = extract_text(uploaded_file)
        st.success("✅ Document Loaded")

    st.markdown("---")
    st.subheader("💾 Ask Anything Memory")
    if st.session_state.qa_memory:
        for i, entry in enumerate(st.session_state.qa_memory):
            with st.expander(f"Q{i+1}: {entry['question'][:40]}..."):
                st.write(f"**Q:** {entry['question']}")
                st.write(f"**A:** {entry['answer']}")
                if st.button(f"❌ Delete Q{i+1}", key=f"delete_{i}"):
                    st.session_state.qa_memory.pop(i)
                    st.experimental_rerun()

        if st.button("🧹 Clear All"):
            st.session_state.qa_memory.clear()
            st.rerun()
    else:
        st.info("No memory yet.")

# -------------------
# 🧩 Main Functional Tabs
# -------------------
if st.session_state.document_text:
    tab1, tab2, tab3 = st.tabs(["📌 Summary", "💬 Ask Anything", "🎯 Challenge Me"])

    # --- SUMMARY ---
    with tab1:
        st.subheader("📌 Document Summary")
        summary = generate_summary(st.session_state.document_text)
        st.success(summary)

    # --- ASK ANYTHING ---
    with tab2:
        st.subheader("💬 Ask Anything Based on the Document")
        question = st.text_input("Enter your question:")
        if st.button("🧠 Get Answer"):
            if question.strip():
                answer = answer_question(st.session_state.document_text, question)
                st.markdown("**📘 Answer:**")
                st.info(answer)
                st.session_state.qa_memory.append({
                    "question": question,
                    "answer": answer
                })
            else:
                st.warning("Please ask something.")

    # --- CHALLENGE ME ---
    with tab3:
        st.subheader("🎯 Challenge Me with Logical Questions")
        if not st.session_state.challenge_questions:
            if st.button("🔄 Generate Questions"):
                st.session_state.challenge_questions = generate_challenge_questions(
                    st.session_state.document_text
                )

        if st.session_state.challenge_questions:
            for i, question in enumerate(st.session_state.challenge_questions):
                st.markdown(f"**Q{i + 1}:** {question}")
                st.text_input("Your Answer:", key=f"user_answer_{i}")

            if st.button("✅ Evaluate My Answers"):
                st.session_state.qa_history = []
                for i, question in enumerate(st.session_state.challenge_questions):
                    answer = st.session_state.get(f"user_answer_{i}", "")
                    if answer.strip():
                        evaluation = evaluate_answer(
                            st.session_state.document_text, question, answer
                        )
                        st.session_state.qa_history.append({
                            "question": question,
                            "user_answer": answer,
                            "evaluation": evaluation
                        })
                    else:
                        st.session_state.qa_history.append({
                            "question": question,
                            "user_answer": "(No answer)",
                            "evaluation": "❌ No answer given."
                        })
                st.rerun()

        if st.session_state.qa_history:
            st.markdown("### 📊 Results")
            for i, item in enumerate(st.session_state.qa_history, 1):
                st.markdown(f"**Q{i}:** {item['question']}")
                st.markdown(f"- 📝 Your Answer: `{item['user_answer']}`")
                st.markdown(f"- 🎯 **Feedback:**")
                st.info(item['evaluation'])
                st.markdown("---")
else:
    st.info("👈 Upload a document from the sidebar to begin.")

# ---------------------------
# 📌 Footer (Credits Section)
# ---------------------------
st.markdown(
    """
    <hr style="margin-top: 30px; border: none; height: 1px; background-color: #ddd;" />
    <div style="text-align: center; color: gray; font-size: 0.9em;">
        🔧 A contribution by <b>Mohammad Ahmad</b> • <a href="https://github.com/Mohammad-Ahmad003" target="_blank">GitHub</a>
    </div>
    """,
    unsafe_allow_html=True
)
