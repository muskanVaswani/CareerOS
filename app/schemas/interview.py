from pydantic import BaseModel, Field

class InterviewPreparation(BaseModel):
    questions: list[str] = Field(default_factory=list)
    