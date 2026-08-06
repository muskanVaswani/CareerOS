from pydantic import BaseModel

class CareerGoal(BaseModel):
    target_role: str
    target_level: str | None = None
    target_company: str | None = None
    
    