def load_skills(file_path="data/skills.txt"):
    with open(file_path, "r", encoding="utf-8") as file:
        return [skill.strip() for skill in file.readlines()]


def analyze_resume(resume_text):
    skills = load_skills()

    resume_lower = resume_text.lower()

    matched = []

    for skill in skills:
        if skill.lower() in resume_lower:
            matched.append(skill)

    score = round((len(matched) / len(skills)) * 100)

    return matched, score