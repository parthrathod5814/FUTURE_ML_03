def generate_resume_summary(
    resume_skills,
    job_skills,
    score
):

    matched = list(set(job_skills) & set(resume_skills))
    missing = list(set(job_skills) - set(resume_skills))

    # Strength analysis
    if len(matched) >= len(job_skills) * 0.7:
        fit_level = "strong alignment with the role requirements"
    elif len(matched) >= len(job_skills) * 0.4:
        fit_level = "moderate alignment with the role"
    else:
        fit_level = "limited alignment with the role requirements"

    strengths_text = (
        f"The candidate demonstrates experience in {', '.join(matched)}."
        if matched else
        "The candidate has limited overlap with required technical skills."
    )

    gap_text = (
        f"However, experience in {', '.join(missing)} appears to be missing."
        if missing else
        "The candidate covers most of the required technical skills."
    )

    final_comment = (
        f"Overall, based on a score of {round(score,3)}, "
        f"the profile shows {fit_level}."
    )

    summary = f"""
    {strengths_text}
    {gap_text}
    {final_comment}
    """

    return summary.strip()
