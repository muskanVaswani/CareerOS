from pydantic import BaseModel


class CareerProfile(BaseModel):
    id: str
    title: str
    description: str
    
    
    core_skills: list[str]
    knowledge_areas: list[str]
    essential_tools: list[str]
    
    project_categories: list[str]
    assessment_skills: list[str]
    prerequisites: list[str]
    
    recommended_certifications: list[str]