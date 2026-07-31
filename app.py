import streamlit as st

from src.resume_parser import extract_text
from src.analyzer import analyze_resume

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="centered"
)

st.title("📄 AI Resume Analyzer")

st.write("Upload your resume and discover which technical skills are detected.")

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

if uploaded_file is not None:

    with st.spinner("Analyzing Resume..."):

        text = extract_text(uploaded_file)

        matched_skills, score = analyze_resume(text)

    st.success("Analysis Completed")

    st.subheader("Resume Score")

    st.progress(score / 100)

    st.metric("Skill Match", f"{score}%")

    st.subheader("Detected Skills")

    if matched_skills:
        for skill in matched_skills:
            st.write(f"✅ {skill}")
    else:
        st.warning("No matching skills found.")