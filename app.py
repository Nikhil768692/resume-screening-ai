import nltk
nltk.download('stopwords')

import streamlit as st
import pandas as pd
from utils import extract_text, rank_resumes

# Configure the Streamlit page
st.set_page_config(page_title="AI Resume Screener", layout="wide")

# Title
st.title("🤖 AI-based Resume Screening System")
st.markdown("Upload resumes and a job description to automatically rank candidates using NLP.")

# Upload resumes
uploaded_files = st.file_uploader(
    "📄 Upload Resumes (PDF or DOCX format)", 
    type=["pdf", "docx"], 
    accept_multiple_files=True
)

# Job description input
job_description = st.text_area("📝 Enter Job Description")

# Trigger button
if st.button("🔍 Rank Resumes"):
    if not uploaded_files or not job_description.strip():
        st.warning("Please upload at least one resume and enter a job description.")
    else:
        resume_texts = []
        file_names = []

        for file in uploaded_files:
            text = extract_text(file)
            if text.strip():  # Skip empty files
                resume_texts.append(text)
                file_names.append(file.name)

        if not resume_texts:
            st.error("❌ Could not extract any text from the uploaded files.")
        else:
            # Rank resumes
            results = rank_resumes(resume_texts, job_description)
            df_results = pd.DataFrame({
                "Resume": file_names,
                "Match Score (%)": (results * 100).round(2)  # Convert to percentage
            }).sort_values(by="Match Score (%)", ascending=False)

            # Show results
            st.success("✅ Ranking Complete!")
            st.dataframe(df_results.reset_index(drop=True), use_container_width=True)

            # Download CSV
            csv = df_results.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="📥 Download Ranked Results as CSV",
                data=csv,
                file_name="ranked_resumes.csv",
                mime="text/csv"
            )
