def analyze_readme(readme: str):

    if not readme:
        return {
            "technologies": [],
            "has_installation": False,
            "has_usage": False,
            "quality_score": 0
        }

    text = readme.lower()

    technologies = []

    keywords = [
        "python",
        "fastapi",
        "flask",
        "django",
        "react",
        "javascript",
        "typescript",
        "postgresql",
        "mysql",
        "mongodb",
        "docker",
        "redis",
        "openai",
        "gemini"
    ]

    for keyword in keywords:
        if keyword in text:
            technologies.append(keyword)

    has_installation = (
        "installation" in text or
        "install" in text
    )

    has_usage = (
        "usage" in text or
        "getting started" in text or
        "how to run" in text
    )

    has_license = "license" in text
    has_contributing = "contributing" in text

    quality_score = 0

    # Project description
    if len(readme) > 100:
        quality_score += 20

    # Technologies mentioned
    quality_score += min(len(set(technologies)) * 5, 25)

    # Installation guide
    if has_installation:
        quality_score += 20

    # Usage guide
    if has_usage:
        quality_score += 20

    # License
    if has_license:
        quality_score += 10

    # Contributing
    if has_contributing:
        quality_score += 5

    quality_score = min(quality_score, 100)

    return {
        "technologies": sorted(set(technologies)),
        "has_installation": has_installation,
        "has_usage": has_usage,
        "has_license": has_license,
        "has_contributing": has_contributing,
        "quality_score": quality_score
    }