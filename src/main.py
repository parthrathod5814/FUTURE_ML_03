import pandas as pd
import matplotlib.pyplot as plt
# import modules
from src.preprocess import clean_text
from src.skills import extract_skills
from src.matcher import compute_similarity

jobs = pd.read_csv("data/jobs_small.csv")

print("\n✅ Dataset loaded!")


jobs["clean_text"] = jobs["Job Description"].apply(clean_text)

print("\n✨ Cleaned text sample:\n")
print(jobs["clean_text"].head())


jobs["skills_found"] = jobs["clean_text"].apply(extract_skills)

print("\n🔥 Extracted skills sample:\n")
print(jobs["skills_found"].head())

print("\n🚀 Resume Matching Demo\n")

resumes = [
    "python supply chain logistics management",
    "architectural design drafting engineering",
    "education training curriculum planning",
    "environmental compliance analysis"
]

job_text = jobs["clean_text"].iloc[0]

scores = compute_similarity(job_text, resumes)

for i, score in enumerate(scores):
    print(f"Candidate {i+1} similarity score:", round(score, 3))

print("\n🧠 Skill Gap Analysis\n")

job_skills = extract_skills(job_text)

for i, resume in enumerate(resumes):

    resume_clean = clean_text(resume)
    resume_skills = extract_skills(resume_clean)

    missing = set(job_skills) - set(resume_skills)
    matched = set(job_skills) & set(resume_skills)

    print(f"\nCandidate {i+1}")
    print("Similarity Score:", round(scores[i], 3))
    print("Matched Skills:", list(matched))
    print("Missing Skills:", list(missing))

print("\n🏆 FINAL CANDIDATE RANKING\n")

ranking = sorted(
    enumerate(scores),
    key=lambda x: x[1],
    reverse=True
)

for rank, (idx, score) in enumerate(ranking, start=1):

    resume_clean = clean_text(resumes[idx])
    resume_skills = extract_skills(resume_clean)

    matched = set(job_skills) & set(resume_skills)
    missing = set(job_skills) - set(resume_skills)

    print(f"Rank #{rank} — Candidate {idx+1}")
    print("Score:", round(score, 3))
    print("Matched Skills:", list(matched))
    print("Missing Skills:", list(missing))
    print("-" * 40)

print("\n🚀 REAL DATASET MATCHING\n")

# choose one job as reference
job_text = jobs["clean_text"].iloc[0]

candidate_resumes = jobs["clean_text"].iloc[1:20].tolist()

scores = compute_similarity(job_text, candidate_resumes)

ranking = sorted(
    enumerate(scores),
    key=lambda x: x[1],
    reverse=True
)

for rank, (idx, score) in enumerate(ranking[:5], start=1):

    resume_text = candidate_resumes[idx]
    resume_skills = extract_skills(resume_text)

    print(f"\nRank #{rank}")
    print("Score:", round(score, 3))
    print("Skills:", resume_skills)

print("\n📊 Ranking Visualization")

top_scores = [score for _, score in ranking[:5]]

plt.figure()
plt.bar(range(1, len(top_scores)+1), top_scores)
plt.title("Top Candidate Similarity Scores")
plt.xlabel("Candidate Rank")
plt.ylabel("Score")
plt.show()