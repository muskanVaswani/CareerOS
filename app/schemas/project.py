from pydantic import BaseModel, Field


class ProjectRecommendations(BaseModel):
    projects: list[str] = Field(default_factory=list)