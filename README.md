# 🤖 AI-based Resume Screening System

An AI-powered resume screening tool that ranks resumes based on a job description using Natural Language Processing (NLP). Built with Python and Streamlit, this tool helps HR teams automate candidate filtering and save time.

---

## 🚀 Features

- 📄 Upload multiple resumes (PDF or DOCX)
- 📝 Paste or type a job description
- 🧠 Uses NLP to extract and compare keywords
- 📊 Ranks resumes by relevance score
- 📥 Download ranked results as CSV
- 🌐 Deployed using Streamlit Cloud

---

## 🧰 Tech Stack

- **Frontend/UI**: [Streamlit](https://streamlit.io/)
- **NLP**: SpaCy, NLTK
- **ML**: Scikit-learn (TF-IDF + Cosine Similarity)
- **PDF/DOCX Parsing**: PyPDF2, python-docx
- **Data Handling**: Pandas

---

## 🖼 Demo

[Click here to try the app](https://your-streamlit-app-url.streamlit.app)  

---

## 🛠 How It Works

1. **Resume Parsing**: Text is extracted from uploaded resumes using PDF or DOCX parsers.
2. **Job Description Input**: The user provides a job description in text form.
3. **Preprocessing**: 
   - Lemmatization (SpaCy)
   - Stopword removal (NLTK)
4. **Similarity Calculation**: 
   - TF-IDF vectorization
   - Cosine similarity between resumes and job description
5. **Ranking**: Resumes are sorted based on similarity score.
