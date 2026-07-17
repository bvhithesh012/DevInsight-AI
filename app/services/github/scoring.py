def calculate_github_score(stats: dict):

    score = 0

    # Repository count (max 30)
    score += min(stats["total_repositories"] * 3, 30)

    # Stars (max 20)
    score += min(stats["total_stars"] * 2, 20)

    # Forks (max 10)
    score += min(stats["total_forks"] * 2, 10)

    # Language diversity (max 15)
    score += min(len(stats["language_distribution"]) * 3, 15)

    # AI Projects (max 10)
    score += min(stats["ai_projects"] * 5, 10)

    # Backend Projects (max 10)
    score += min(stats["backend_projects"] * 2, 10)

    # Frontend Projects (max 5)
    score += min(stats["frontend_projects"] * 1, 5)

    return min(score, 100)