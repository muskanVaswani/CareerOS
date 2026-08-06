from pydantic import BaseModel


class LearningPreferences(BaseModel):
    hours_per_week: int | None = None
    
    target_duration: int | None = None
    
    budget:float | None = None
    
    preferred_learning_style: str | None = None
    
    preferred_language: str | None = None
    
    project_based_learning: bool = True