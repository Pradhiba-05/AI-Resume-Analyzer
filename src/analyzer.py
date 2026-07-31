def load_skills(file_path="data/skills.txt"):
    """
    Load all technical skills from skills.txt
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return [skill.strip() for skill in file.readlines() if skill.strip()]


def analyze_resume(resume_text):
    """
    Analyze resume text and return matched skills and score.
    """

    skills = load_skills()

    resume_lower = resume_text.lower()

    matched_skills = []

    for skill in skills:
        if skill.lower() in resume_lower:
            matched_skills.append(skill)

    score = round((len(matched_skills) / len(skills)) * 100)

    return matched_skills, score