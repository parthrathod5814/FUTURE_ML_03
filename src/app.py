import streamlit as st
import base64

from preprocess import clean_text
from skills import extract_skills
from matcher import compute_final_scores
from pdf_reader import extract_text_from_pdf
from summary_generator import generate_resume_summary


st.set_page_config(layout="wide")
st.title("📄 AI Resume Screening System")

if "open_resume" not in st.session_state:
    st.session_state.open_resume = None

st.subheader("🎯 Enter Job Description")

job_input = st.text_area(
    "Paste job role description here",
    height=200
)

job_text = ""
job_skills = []

if job_input:
    job_text = clean_text(job_input)
    job_skills = extract_skills(job_text)

    st.success("Required Skills Detected:")
    st.write(" • " + "\n • ".join(job_skills))

st.subheader("📄 Upload Resume PDFs")

uploaded_files = st.file_uploader(
    "Upload multiple resumes",
    type=["pdf"],
    accept_multiple_files=True
)

resume_texts = []

if uploaded_files:
    for file in uploaded_files:
        text = extract_text_from_pdf(file)
        resume_texts.append(text)


if job_text and resume_texts:

    st.markdown("---")
    st.header("🚀 Candidate Ranking Dashboard")

    clean_resumes = [clean_text(t) for t in resume_texts]

    scores = compute_final_scores(
        job_text,
        job_skills,
        clean_resumes,
        extract_skills
    )

    ranking = sorted(
        enumerate(scores),
        key=lambda x: x[1],
        reverse=True
    )

    for rank, (idx, score) in enumerate(ranking, start=1):

        resume_skills = extract_skills(clean_resumes[idx])

        matched = list(set(job_skills) & set(resume_skills))
        missing = list(set(job_skills) - set(resume_skills))

        # Category
        if score >= 0.65:
            category = "🟢 Strong Fit"
        elif score >= 0.45:
            category = "🟡 Good Fit"
        else:
            category = "🔴 Weak Fit"

        st.markdown(f"## Rank #{rank} — {uploaded_files[idx].name}")
        st.markdown(f"**Category:** {category}")
        st.progress(min(score, 1.0))

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Final Score", round(score, 3))
            st.markdown("### 🟢 Matched Skills")
            for skill in matched:
                st.markdown(f"- {skill.title()}")

        with col2:
            st.markdown("### 🔴 Missing Skills")
            for skill in missing:
                st.markdown(f"- {skill.title()}")

        summary = generate_resume_summary(
            resume_skills,
            job_skills,
            score
        )

        st.markdown("### 🧠 AI Resume Summary")
        st.info(summary)

        if st.session_state.open_resume == idx:
            if st.button(f"❌ Close Resume — {uploaded_files[idx].name}", key=f"close_{idx}"):
                st.session_state.open_resume = None
        else:
            if st.button(f"👁️ View Resume — {uploaded_files[idx].name}", key=f"open_{idx}"):
                st.session_state.open_resume = idx

        if st.session_state.open_resume == idx:
            pdf_bytes = uploaded_files[idx].getvalue()
            base64_pdf = base64.b64encode(pdf_bytes).decode("utf-8")

            pdf_display = f"""
                <iframe src="data:application/pdf;base64,{base64_pdf}"
                width="100%" height="700px"></iframe>
            """

            st.markdown(pdf_display, unsafe_allow_html=True)

        st.markdown("---")
