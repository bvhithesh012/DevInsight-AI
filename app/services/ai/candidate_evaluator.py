from app.services.ai.gemini_service import generate_response


def evaluate_candidate(candidate_profile: dict):

    prompt = f"""
You are an expert technical recruiter.

Evaluate the following candidate profile.

{candidate_profile}

Return:

1. Overall Score (0-100)
2. Technical Strengths
3. Weaknesses
4. Missing Skills
5. Project Evaluation
6. GitHub Evaluation
7. Resume Quality
8. Hiring Recommendation
9. Improvement Suggestions
"""

    return generate_response(prompt)