from pydantic import BaseModel

from app.schemas.career_goal import CareerGoal
from app.schemas.learning_preferences import LearningPreferences


class Request(BaseModel):
    career_goal: CareerGoal
    learning_preferences: LearningPreferences
    