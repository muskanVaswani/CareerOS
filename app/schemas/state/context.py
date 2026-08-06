from pydantic import BaseModel

from app.schemas.profile import Profile



class Context(BaseModel):
    profile: Profile | None = None
    