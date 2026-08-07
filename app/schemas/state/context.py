from pydantic import BaseModel

from app.schemas.profile import Profile
from app.schemas.career_profile import CareerProfile



class Context(BaseModel):
    profile: Profile | None = None
    career_profile: CareerProfile | None = None