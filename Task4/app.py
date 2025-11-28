# import streamlit as st
# from dotenv import load_dotenv

# from modules.pdf_handler import extract_text_from_pdf
# from modules.ai_engine import generate_summary, generate_quiz
# from modules.ui_components import (
#     layout_header, upload_section, show_summary,
#     show_loader, footer
# )

# load_dotenv()

# st.set_page_config(page_title="📚 Study Mate", layout="wide")

# layout_header()

# uploaded_file = upload_section()


# # ---------------- SESSION STATE ----------------
# st.session_state.setdefault("pdf_text", None)
# st.session_state.setdefault("summary", None)
# st.session_state.setdefault("quiz_questions", None)
# st.session_state.setdefault("user_answers", {})


# # ---------------- AFTER PDF UPLOAD ----------------
# if uploaded_file:
#     st.success("📄 PDF Uploaded Successfully!")

#     if not st.session_state.pdf_text:
#         st.session_state.pdf_text = extract_text_from_pdf(uploaded_file)

#     if st.button("📝 Generate Summary"):
#         with show_loader("Generating Summary..."):
#             st.session_state.summary = generate_summary(st.session_state.pdf_text)

#     if st.session_state.summary:
#         show_summary(st.session_state.summary)

#         if st.button("🧠 Generate MCQs"):
#             with show_loader("Generating Quiz..."):
#                 raw_quiz = generate_quiz(st.session_state.pdf_text, "Multiple Choice")

#                 questions = []
#                 for block in raw_quiz.split("\n\n"):
#                     lines = [l.strip() for l in block.split("\n") if l.strip()]
#                     if len(lines) >= 6 and "A)" in block:
#                         questions.append({
#                             "question": lines[0],
#                             "options": lines[1:5],
#                             "answer": lines[-1].replace("Answer:", "").strip()
#                         })

#                 st.session_state.quiz_questions = questions


#     # --------------- RENDER QUIZ ----------------
#     if st.session_state.quiz_questions:

#         st.subheader("📝 Quiz Section:")

#         for idx, q in enumerate(st.session_state.quiz_questions):
#             st.write(f"**{idx+1}. {q['question']}**")

#             selected = st.radio(
#                 f"Choose answer:",
#                 q["options"],
#                 key=f"q{idx}"
#             )
#             st.session_state.user_answers[idx] = selected

#         if st.button("✅ Submit Quiz"):
#             score = 0

#             st.subheader("📌 Results:")

#             for i, q in enumerate(st.session_state.quiz_questions):
#                 user = st.session_state.user_answers.get(i)
#                 correct = q["answer"]

#                 user_answer_clean = user.split(")")[0].strip()[0] if user else ""
#                 correct_clean = correct.strip()

#                 if user_answer_clean.lower() == correct_clean.lower():
#                     st.success(f"✔ Q{i+1}: Correct!")
#                     score += 1
#                 else:
#                     st.error(f"❌ Q{i+1}: Wrong — Correct Answer: {correct}")

#             st.info(f"🎯 Final Score: {score} / {len(st.session_state.quiz_questions)}")


# footer()

import streamlit as st
from dotenv import load_dotenv

from modules.pdf_handler import extract_text_from_pdf
from modules.ai_engine import generate_summary, generate_quiz
from modules.ui_components import layout_header, upload_section, show_summary, show_loader, footer

load_dotenv()

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="📖 Smart Learner", layout="wide")

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
/* Body background */
body, .main {
    background-color: #f0f3f7;
}

/* Header */
h1, h2, h3 {
    color: #1f2937;
    font-family: 'Segoe UI', sans-serif;
}

/* Remove borders & shadows from all sections */
.section-card, .question-card {
    background-color: #ffffff;
    padding: 20px;
    margin-bottom: 20px;
    border-radius: 12px;
    box-shadow: none !important;  /* Remove shadow */
    border: none !important;      /* Remove border */
}

/* Buttons */
.stButton>button {
    width: 100%;
    background-color: #4f46e5;
    color: white;
    font-weight: 600;
    padding: 12px 0;
    border-radius: 8px;
    border: none;
}
.stButton>button:hover {
    background-color: #4338ca;
}

/* Quiz */
.question-card {
    background-color: #f9fafb;
}

/* Results */
.result-box {
    padding: 14px;
    border-radius: 10px;
    margin-bottom: 12px;
    font-weight: 500;
}
.success { background-color: #e6f4ea; color: #065f46; }
.error { background-color: #fdecea; color: #b91c1c; }
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("<h1 style='text-align:center;'>📖 Smart Learner</h1>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# ---------------- FILE UPLOAD ----------------
st.markdown("<div class='section-card'>", unsafe_allow_html=True)
uploaded_file = upload_section()
st.markdown("</div>", unsafe_allow_html=True)

# ---------------- SESSION STATE ----------------
st.session_state.setdefault("pdf_text", None)
st.session_state.setdefault("summary", None)
st.session_state.setdefault("quiz_questions", None)
st.session_state.setdefault("user_answers", {})

# ---------------- AFTER PDF UPLOAD ----------------
if uploaded_file:
    st.success("📄 PDF Uploaded Successfully!")

    if not st.session_state.pdf_text:
        st.session_state.pdf_text = extract_text_from_pdf(uploaded_file)

    # SUMMARY
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    if st.button("📝 Generate Summary"):
        with show_loader("Generating Summary..."):
            st.session_state.summary = generate_summary(st.session_state.pdf_text)
    st.markdown("</div>", unsafe_allow_html=True)

    # SHOW SUMMARY
    if st.session_state.summary:
        st.markdown("<div class='section-card'>", unsafe_allow_html=True)
        show_summary(st.session_state.summary)
        st.markdown("</div>", unsafe_allow_html=True)

        # GENERATE QUIZ
        st.markdown("<div class='section-card'>", unsafe_allow_html=True)
        if st.button("🧠 Generate MCQs"):
            with show_loader("Generating Quiz..."):
                raw_quiz = generate_quiz(st.session_state.pdf_text, "Multiple Choice")
                questions = []
                for block in raw_quiz.split("\n\n"):
                    lines = [l.strip() for l in block.split("\n") if l.strip()]
                    if len(lines) >= 6 and "A)" in block:
                        questions.append({
                            "question": lines[0],
                            "options": lines[1:5],
                            "answer": lines[-1].replace("Answer:", "").strip()
                        })
                st.session_state.quiz_questions = questions
        st.markdown("</div>", unsafe_allow_html=True)

    # QUIZ SECTION
    if st.session_state.quiz_questions:
        st.subheader("📝 Quiz Section")
        for idx, q in enumerate(st.session_state.quiz_questions):
            st.markdown("<div class='question-card'>", unsafe_allow_html=True)
            st.write(f"**{idx+1}. {q['question']}**")
            selected = st.radio(f"Choose answer:", q["options"], key=f"q{idx}")
            st.session_state.user_answers[idx] = selected
            st.markdown("</div>", unsafe_allow_html=True)

        # SUBMIT QUIZ
        st.markdown("<div class='section-card'>", unsafe_allow_html=True)
        if st.button("✅ Submit Quiz"):
            score = 0
            st.subheader("📌 Results")
            for i, q in enumerate(st.session_state.quiz_questions):
                user = st.session_state.user_answers.get(i)
                correct = q["answer"]
                user_answer_clean = user.split(")")[0].strip()[0] if user else ""
                correct_clean = correct.strip()
                if user_answer_clean.lower() == correct_clean.lower():
                    st.markdown(f"<div class='result-box success'>✔ Q{i+1}: Correct!</div>", unsafe_allow_html=True)
                    score += 1
                else:
                    st.markdown(f"<div class='result-box error'>❌ Q{i+1}: Wrong — Correct Answer: {correct}</div>", unsafe_allow_html=True)
            st.info(f"🎯 Final Score: **{score} / {len(st.session_state.quiz_questions)}**")
        st.markdown("</div>", unsafe_allow_html=True)

footer()
