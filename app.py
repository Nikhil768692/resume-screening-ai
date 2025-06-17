import streamlit as st
from utils import extract_text, rank_resumes
import os
import pandas as pd

# Page config
st.set_page_config(page_title="AI Resume Screener", layout="wide")

# Title
st.title("🤖 AI-based Resume Screening System")
st.markdown("Upload resumes and a job description to automatically rank candidates using NLP.")

# File upload
uploaded_files = st.file_uploader("📄 Upload Resumes (PDF format)", type=["pdf"], accept_multiple_files=True)
job_description = st.text_area("📝 Enter Job Description")

# Process
if st.button("🔍 Rank Resumes"):
    if not uploaded_files or not job_description.strip():
        st.warning("Please upload at least one resume and enter a job description.")
    else:
        resume_texts = []
        file_names = []

        # Extract text from resumes
        for file in uploaded_files:
            text = extract_text(file)
            resume_texts.append(text)
            file_names.append(file.name)

        # Rank resumes
        results = rank_resumes(resume_texts, job_description)
        df_results = pd.DataFrame({
            "Resume": file_names,
            "Match Score (%)": results
        }).sort_values(by="Match Score (%)", ascending=False)

        st.success("✅ Ranking Complete!")
        st.dataframe(df_results.reset_index(drop=True), use_container_width=True)

        # Download button
        csv = df_results.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Ranked Results as CSV",
            data=csv,
            file_name="ranked_resumes.csv",
            mime="text/csv"
        )
