# from typing import Any




# from app.schemas.interview import InterviewPreparation
# from app.schemas.state.metadata import Metadata
# from app.schemas.profile import Profile
# from app.schemas.project import ProjectRecommendations
# from app.schemas.recruiter_feedback import RecruiterFeedback
# from app.schemas.roadmap import Roadmap
# from app.schemas.skill_gap import SkillGap


from pydantic import BaseModel, Field


from app.schemas.state.request import Request
from app.schemas.state.context import Context
from app.schemas.state.results import Results 
from app.schemas.state.metadata import Metadata



class CareerState(BaseModel):
    # user_input: str
    
    # profile: dict[str, Any] | None = None
    # skill_gap: dict[str, Any] | None = None
    # roadmap: dict[str, Any] | None = None
    # projects: dict[str, Any] | None = None
    # interview: dict[str, Any] | None = None
    # recruiter_feedback: dict[str, Any] | None = None
    # metadata: Metadata = Metadata()
    
    
    request: Request
    
    context: Context = Field(default_factory=Context)
    results: Results = Field(default_factory=Results)
    metadata: Metadata = Field(default_factory=Metadata)
    