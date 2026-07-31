import streamlit as st

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖",
    layout="wide"
)

with open("styles/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("""
<div class="hero-title">
🤖 AI Resume Analyzer 
</div>

<div class="hero-subtitle">
Analyze your resume with AI-powered insights, ATS scoring and career recommendations.
</div>
""", unsafe_allow_html=True)

st.file_uploader(
    "📄 Upload Resume",
    type=["pdf"]
)

st.markdown("<br>", unsafe_allow_html=True)

col1,col2,col3,col4=st.columns(4)

with col1:
    st.markdown("""
    <div class="card">
    <h2>📊</h2>
    <h3>Resume Score</h3>
    <p>AI-based evaluation</p>
    </div>
    """,unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
    <h2>🎯</h2>
    <h3>ATS Score</h3>
    <p>Recruiter friendly</p>
    </div>
    """,unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
    <h2>💼</h2>
    <h3>Job Match</h3>
    <p>Recommended roles</p>
    </div>
    """,unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="card">
    <h2>🚀</h2>
    <h3>AI Suggestions</h3>
    <p>Improve your resume</p>
    </div>
    """,unsafe_allow_html=True)

st.markdown("---")

st.markdown("## 📈 Platform Statistics")

s1,s2,s3,s4=st.columns(4)

with s1:
    st.markdown("""
<div class="stats">
<h1>100+</h1>
<p>Supported Skills</p>
</div>
""",unsafe_allow_html=True)

with s2:
    st.markdown("""
<div class="stats">
<h1>95%</h1>
<p>ATS Accuracy</p>
</div>
""",unsafe_allow_html=True)

with s3:
    st.markdown("""
<div class="stats">
<h1>10K+</h1>
<p>Resumes Analyzed</p>
</div>
""",unsafe_allow_html=True)

with s4:
    st.markdown("""
<div class="stats">
<h1>24/7</h1>
<p>AI Assistance</p>
</div>
""",unsafe_allow_html=True)