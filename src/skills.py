skills_db = [
 
    "python", "sql", "machine learning", "data analysis",
    "nlp", "cloud", "excel",
    "management", "leadership", "communication",
    "project management", "coordination",
    "architecture", "design", "drafting",
    "supply chain", "logistics", "inventory",
    "environmental analysis", "compliance",
    "education", "training", "curriculum"
]

def extract_skills(text):
    found = []

    for skill in skills_db:
        if skill in text:
            found.append(skill)

    return found
