from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
from app.services.parser_service import extract_pdf_text, parse_resume

from app.database.connection import get_db
from app.models.resume import Resume
from app.schemas.resume import ResumeResponse
from app.services.file_service import save_file

router = APIRouter(
    prefix="/resume",
    tags=["Resume"]
)


@router.post("/upload")
def upload_resume(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    # Save file
    file_path = save_file(file)

    # Save metadata
    resume = Resume(
        user_id=1,
        file_name=file.filename,
        file_path=file_path,
        file_type=file.filename.split(".")[-1]
    )

    db.add(resume)
    db.commit()
    db.refresh(resume)

    # Extract text
    if file.filename.lower().endswith(".pdf"):
        text = extract_pdf_text(file_path)
    else:
        return {
            "error": "Only PDF support added for now."
        }

    # Parse resume
    parsed_data = parse_resume(text)

    return {
        "resume_id": resume.id,
        "file_name": resume.file_name,
        "parsed_data": parsed_data
    }