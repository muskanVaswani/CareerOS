from pydantic import BaseModel, Field

class RoadmapPhase(BaseModel):
    phase: int
    title: str
    topics: list[str] = Field(default_factory=list)
    depth: str
    estimated_weeks: int | None = None
    project: str | None = None
    
    
class Roadmap(BaseModel):
    goal: str
    depth: str
    phases: list[RoadmapPhase] = Field(default_factory=list)
     