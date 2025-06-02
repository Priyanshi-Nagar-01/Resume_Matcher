import streamlit as st
from parsers.text_extractor import extract_text
from parsers.resume_parser import parse_resume
from parsers.matcher import compute_similarity

st.set_page_config(page_title="Smart Resume Parser + Job Matcher", layout="wide")
st.title("Smart Resume Parser + Job Matcher (Improved Version)")

uploaded_resume = st.file_uploader("Upload your Resume (PDF, DOCX, TXT)", type=["pdf", "docx", "txt"])
uploaded_job = st.file_uploader("Upload Job Description (TXT, PDF, DOCX)", type=["txt", "pdf", "docx"])

if uploaded_resume and uploaded_job:
    resume_text = extract_text(uploaded_resume)
    job_text = extract_text(uploaded_job)

    resume_data = parse_resume(resume_text)
    job_data = parse_resume(job_text)

    st.subheader("Extracted Resume Skills")
    st.write(resume_data["skills"])

    st.subheader("Extracted Job Description Skills")
    st.write(job_data["skills"])

    score = compute_similarity(resume_data["skills"], job_data["skills"])
    st.subheader("Match Score")
    st.write(f"{score*100:.2f}%")

    if score > 0.7:
        st.success("Great match! You are well suited for this job.")
    elif score > 0.4:
        st.warning("Moderate match. Consider improving relevant skills.")
    else:
        st.error("Low match. Consider acquiring relevant skills for this job.")
else:
    st.info("Please upload both your resume and the job description.")
