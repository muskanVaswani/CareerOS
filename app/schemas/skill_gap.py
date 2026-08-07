from pydantic import BaseModel, Field


class SkillGap(BaseModel):
    matched_core_skills: list[str] = Field(default_factory=list)
    missing_core_skills: list[str] = Field(default_factory=list)
    knowledge_gaps: list[str] = Field(default_factory=list)
    missing_knowledge: list[str] = Field(default_factory=list)
    completion_percentage: float = 0.0