# 📄 AI Resume Screening System

An AI-powered Resume Screening and Candidate Ranking System built using NLP and Machine Learning techniques.

This project simulates a real-world Applicant Tracking System (ATS) that evaluates multiple resumes against a recruiter-provided job description and ranks candidates based on role fit using a hybrid scoring model.

---

## 🚀 Project Motivation

Recruiters often receive hundreds of resumes for a single role.

Manual screening is:
- Time-consuming
- Inconsistent
- Biased
- Error-prone

Most basic ATS systems rely only on keyword matching, which fails to capture contextual relevance.

This system improves upon that by combining:
- Text similarity scoring
- Structured skill extraction
- Skill-weighted ranking logic
- Candidate categorization
- AI-generated evaluation summaries

---

## 🎯 Problem Statement

How can we automatically evaluate resumes in a way that:

- Identifies relevant candidates quickly
- Detects missing required skills
- Balances contextual similarity with explicit skill matching
- Produces explainable ranking outputs for recruiters

---

## 🧠 System Architecture

The system follows a modular NLP pipeline:

1️⃣ **Input Layer**
- Recruiter enters job description
- Multiple resume PDFs are uploaded

2️⃣ **Text Processing Layer**
- PDF text extraction (PyMuPDF)
- Lowercasing, cleaning, normalization
- NLP preprocessing using spaCy

3️⃣ **Feature Engineering**
- TF-IDF vectorization
- Skill extraction engine
- Skill matching logic

4️⃣ **Hybrid Scoring Engine**

Final Score =

0.6 × Text Similarity (TF-IDF Cosine Similarity)  
+ 0.4 × Skill Match Ratio  

Where:

- Text Similarity captures contextual alignment
- Skill Match Ratio ensures required skill overlap
- Balanced weighting improves ranking fairness

5️⃣ **Output Layer**
- Ranked candidates
- Skill gap analysis
- Candidate categorization
- AI-generated summary
- Resume viewer dashboard

---

## 📊 Hybrid Scoring Strategy

Unlike simple keyword matching, this system:

✔ Uses TF-IDF + cosine similarity for contextual relevance  
✔ Extracts structured skill entities  
✔ Computes explicit skill overlap  
✔ Combines both into a weighted ranking model  
✔ Produces interpretable outputs  

This creates a more balanced evaluation compared to pure keyword systems.

---

## 📈 Candidate Evaluation Output

For each candidate, the system generates:

- Final Score
- Skill Match Ratio
- Matched Skills
- Missing Skills
- Category (Strong / Good / Weak Fit)
- AI-generated resume summary
- Full resume viewer

This makes the system recruiter-friendly and decision-support oriented.

---

## 📊 Key Features

- 📌 Job description input
- 📄 Multi-PDF resume upload
- 🧠 NLP-based preprocessing
- 📊 TF-IDF similarity scoring
- 🎯 Skill-weighted ranking model
- 🟢 Candidate categorization
- ⚠ Skill gap detection
- 🧠 AI-generated summary engine
- 👁 Interactive resume viewing

---

## 📁 Project Structure

```
FUTURE_ML_03/
│
├── src/
│   ├── app.py                # Streamlit application
│   ├── preprocess.py         # Text cleaning pipeline
│   ├── matcher.py            # Scoring & similarity engine
│   ├── skills.py             # Skill extraction logic
│   ├── pdf_reader.py         # Resume PDF parsing
│   ├── summary_generator.py  # AI summary generation
│
├── data/
│   └── jobs_small.csv
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 📊 Dataset Used

For job role analysis and skill vocabulary reference:

Resume Entities & Job Roles Dataset  
https://www.kaggle.com/datasets/ravindrasinghrana/job-description-dataset  

Used for:
- Job description structure understanding
- Skill extraction experimentation
- NLP preprocessing practice

---

## ⚙ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Sharankohli/FUTURE_ML_03.git
cd FUTURE_ML_03
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Download spaCy Model

```bash
python -m spacy download en_core_web_sm
```

### 5️⃣ Run Application

```bash
streamlit run src/app.py
```

---

## 🛠 Technology Stack

- Python
- Streamlit
- Scikit-learn (TF-IDF, Cosine Similarity)
- spaCy (NLP preprocessing)
- PyMuPDF (PDF parsing)
- Custom Skill Extraction Engine
- Hybrid Scoring Model

---

## 📌 Future Improvements

- Transformer-based semantic embeddings
- GPT-powered intelligent resume summaries
- Skill importance weighting by job role
- Resume keyword highlighting
- Exportable recruiter reports (CSV/PDF)
- Role-based evaluation templates

---

## 👨‍💻 Author

Rathod Parth Ashokbhai 


Machine Learning Intern – Future Interns (2026)


