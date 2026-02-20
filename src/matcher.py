from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def compute_similarity(job_text, resumes):

    vectorizer = TfidfVectorizer()

    documents = resumes + [job_text]

    tfidf_matrix = vectorizer.fit_transform(documents)

    scores = cosine_similarity(
        tfidf_matrix[-1],
        tfidf_matrix[:-1]
    )

    return scores[0]


def compute_final_scores(job_text, job_skills, resumes, extract_skills):

    text_scores = compute_similarity(job_text, resumes)

    final_scores = []

    for i, resume in enumerate(resumes):

        resume_skills = extract_skills(resume)

        if len(job_skills) > 0:
            skill_score = len(set(job_skills) & set(resume_skills)) / len(job_skills)
        else:
            skill_score = 0

        final_score = 0.6 * text_scores[i] + 0.4 * skill_score

        final_scores.append(final_score)

    return final_scores
