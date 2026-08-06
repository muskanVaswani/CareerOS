from pydantic import BaseModel, Field

class Profile(BaseModel):
    name: str | None = None
    target_role: str | None = None
    
    education: str | None = None
    experience: int | None = None
    
    skills: list[str] = Field(default_factory=list)
    
    