from pydantic import BaseModel

class RecruiterFeedback(BaseModel):
    feedback: str | None = None