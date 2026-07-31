import streamlit as st

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖",
    layout="wide",
)

st.markdown("""
<style>

.main{
    background:#0f172a;
}

.title{
    text-align:center;
    font-size:55px;
    font-weight:bold;
    color:white;
    margin-top:20px;
}

.subtitle{
    text-align:center;
    font-size:22px;
    color:#94a3b8;
    margin-bottom:40px;
}

.card{
    background:#1e293b;
    padding:25px;
    border-radius:15px;
    border:1px solid #334155;
    margin-top:20px;
}

.feature{
    text-align:center;
    color:white;
    font-size:20px;
}

</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">AI Resume Analyzer</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="subtitle">Analyze resumes with AI-inspired insights and ATS scoring</div>',
    unsafe_allow_html=True,
)

uploaded_file = st.file_uploader(
    "📄 Upload Your Resume (PDF)",
    type=["pdf"],
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
    <div class="feature">
    📊<br><br>
    Resume Score
    </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
    <div class="feature">
    🎯<br><br>
    ATS Analysis
    </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
    <div class="feature">
    💡<br><br>
    AI Suggestions
    </div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

st.markdown("### 🚀 Features")

st.success("✔ Resume Parsing")
st.success("✔ Skill Detection")
st.success("✔ ATS Compatibility")
st.success("✔ Resume Strength Score")
st.success("✔ Career Recommendations")
st.success("✔ Download Analysis Report")