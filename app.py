import streamlit as st
from src.resume_parser import extract_text
from src.analyzer import analyze_resume

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Resume Analyzer ",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------
# Load Custom CSS
# -----------------------------
with open("styles/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -----------------------------
# Sidebar
# -----------------------------

st.sidebar.title("🤖 AI Resume Analyzer")

st.sidebar.markdown("---")

st.sidebar.subheader("📌 Quick Guide")

st.sidebar.markdown("""
1. 📄 Upload your resume (PDF)

2. 🚀 Click **Analyze Resume**

3. 📊 View Resume Score

4. 🎯 Check ATS Score

5. 💼 Explore Career Suggestions
""")

st.sidebar.markdown("---")

st.sidebar.subheader("💡 Resume Tips")

st.sidebar.info("✔ Keep your resume to 1–2 pages.")

st.sidebar.info("✔ Mention measurable achievements.")

st.sidebar.info("✔ Include technical skills.")

st.sidebar.info("✔ Add GitHub & LinkedIn profile.")

st.sidebar.info("✔ Save your resume as PDF.")

st.sidebar.markdown("---")

st.sidebar.markdown("""
<div style="text-align:center; padding-top:10px; color:#94a3b8; font-size:13px;">
🚀 Version 1.0
</div>
""", unsafe_allow_html=True)
# -----------------------------
# Hero Section
# -----------------------------
st.markdown("""
<div class="hero-title">
 AI Resume Analyzer
</div>

<div class="hero-subtitle">
Discover your resume's strengths, identify missing skills, improve ATS compatibility, and unlock personalized career recommendations—all in seconds.
</div>
""", unsafe_allow_html=True)

# -----------------------------
# File Upload
# -----------------------------
uploaded_file = st.file_uploader(
    "📄 Upload Resume (PDF)",
    type=["pdf"]
)

if uploaded_file:

    st.success("✅ Resume uploaded successfully!")

    col1, col2 = st.columns(2)

    with col1:
        st.info(f"**📄 File Name:** {uploaded_file.name}")

    with col2:
        st.info(f"**📦 Size:** {round(uploaded_file.size/1024,2)} KB")

    st.markdown("<br>", unsafe_allow_html=True)

    left, right = st.columns([1, 2])

    with left:

        if st.button("🚀 Analyze Resume", use_container_width=True):

            with st.spinner("Analyzing Resume..."):

                resume_text = extract_text(uploaded_file)

                if not resume_text:
                    st.error("❌ Unable to extract text from this PDF.")
                    st.stop()

                matched_skills, score = analyze_resume(resume_text)

                ats_score = min(score + 15, 100)

            st.success("✅ Analysis Completed!")

            metric1, metric2 = st.columns(2)

            with metric1:
                st.metric("📊 Resume Score", f"{score}%")

            with metric2:
                st.metric("🎯 ATS Score", f"{ats_score}%")

            st.progress(score / 100)

            st.subheader("✅ Detected Skills")

            if matched_skills:
                cols = st.columns(3)

                for i, skill in enumerate(matched_skills):
                    cols[i % 3].success(skill)
            else:
                st.warning("No matching skills found.")

            st.subheader("💼 Recommended Careers")

            careers = []

            if "Python" in matched_skills:
                careers.append("🐍 Python Developer")

            if "SQL" in matched_skills:
                careers.append("📊 Data Analyst")

            if "FastAPI" in matched_skills:
                careers.append("⚡ Backend Developer")

            if "Machine Learning" in matched_skills:
                careers.append("🤖 Machine Learning Engineer")

            if "React" in matched_skills:
                careers.append("💻 Full Stack Developer")

            if careers:
                for career in careers:
                    st.success(career)
            else:
                st.info("Add more technical skills to receive career recommendations.")

            st.subheader("🤖 AI Suggestions")

            suggestions = []

            if score < 40:
                suggestions.append("Improve your technical skills section.")

            if "Git" not in matched_skills:
                suggestions.append("Mention Git & GitHub experience.")

            if "Docker" not in matched_skills:
                suggestions.append("Learning Docker can improve your resume.")

            if "AWS" not in matched_skills:
                suggestions.append("Learning AWS can improve your employability.")

            for suggestion in suggestions:
                st.info(suggestion)

        if st.button("🔄 Analyze Another Resume", use_container_width=True):
            st.rerun()

    with right:

        st.markdown("""
        <div class="card">
            <h2>📋 Resume Analysis</h2>
            <hr>
            <p>Upload your resume and click <b>Analyze Resume</b>.</p>
            <p>✔ Resume Score</p>
            <p>✔ ATS Score</p>
            <p>✔ Skill Detection</p>
            <p>✔ Career Recommendations</p>
            <p>✔ AI Suggestions</p>
        </div>
        """, unsafe_allow_html=True)

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")

st.markdown(
"""
<div style="text-align:center;padding:20px;color:#94a3b8;font-size:15px;">
Made with ❤️ using Python • Streamlit 

<br>

© 2026 AI Resume Analyzer 
</div>
""",
unsafe_allow_html=True
)