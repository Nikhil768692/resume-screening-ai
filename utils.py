import subprocess
import sys
import spacy
import PyPDF2
import docx
import pandas as pd
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download and load spaCy model safely
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    subprocess.run([sys.executable, "-m", "spacy", "download", "en_core_web_sm"])
    nlp = spacy.load("en_core_web_sm")

# Download NLTK stopwords if not present
nltk.download("stopwords")
stop_words = set(stopwords.words("english"))

# Extract text from PDF
def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    return " ".join([page.extract_text() for page in reader.pages if page.extract_text()])

# Extract text from DOCX
def extract_text_from_docx(file):
    doc = docx.Document(file)
    return " ".join([para.text for para in doc.paragraphs])

# Handle both file types
def extract_text(file):
    if file.name.endswith(".pdf"):
        return extract_text_from_pdf(file)
    elif file.name.endswith(".docx"):
        return extract_text_from_docx(file)
    else:
        return ""

# Preprocess text: lowercase, lemmatize, remove stopwords
def preprocess(text):
    doc = nlp(text.lower())
    return " ".join([token.lemma_ for token in doc if token.is_alpha and token.text not in stop_words])

# Rank resumes based on similarity to job description
def rank_resumes(resume_texts, job_desc):
    preprocessed_resumes = [preprocess(text) for text in resume_texts]
    preprocessed_job = preprocess(job_desc)
    documents = preprocessed_resumes + [preprocessed_job]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)
    scores = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1]).flatten()

    return scores
