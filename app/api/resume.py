from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
from app.services.parser.resume_parser import parse_resume

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

    if not file.filename.lower().endswith(".pdf"):
      return {
        "error": "Only PDF files are supported for now."
    }

    parsed_data = parse_resume(file_path)
    return {
        "resume_id": resume.id,
        "file_name": resume.file_name,
        "parsed_data": parsed_data
    }