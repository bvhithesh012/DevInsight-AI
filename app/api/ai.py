from fastapi import APIRouter

from app.services.ai.candidate_evaluator import evaluate_candidate

router = APIRouter(
    prefix="/ai",
    tags=["AI"]
)


@router.post("/evaluate-candidate")
def evaluate(profile: dict):

    result = evaluate_candidate(profile)

    return result