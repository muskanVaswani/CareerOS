from pydantic import BaseModel


from app.schemas.skill_gap import SkillGap
from app.schemas.roadmap import Roadmap
from app.schemas.project import ProjectRecommendations
from app.schemas.interview import InterviewPreparation
from app.schemas.recruiter_feedback import RecruiterFeedback


class Results(BaseModel):
    skill_gap: SkillGap | None = None
    roadmap: Roadmap | None = None
    projects: ProjectRecommendations | None = None
    interview: InterviewPreparation | None = None
    recruiter_feedback: RecruiterFeedback | None = None
    