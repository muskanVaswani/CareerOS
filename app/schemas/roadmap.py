from pydantic import BaseModel, Field

class Roadmap(BaseModel):
    phases: list[str] = Field(default_factory=list)