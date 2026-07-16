from pydantic import BaseModel
from datetime import datetime


class ResumeResponse(BaseModel):
    id: int
    file_name: str
    file_type: str
    uploaded_at: datetime

    model_config = {
        "from_attributes": True
    }