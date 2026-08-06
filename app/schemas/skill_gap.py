from pydantic import BaseModel, Field


class SkillGap(BaseModel):
    missing_skills: list[str] = Field(default_factory=list)
    matched_skills: list[str] = Field(default_factory=list)
    completion_percentage: float | None = None