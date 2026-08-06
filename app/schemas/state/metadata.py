from pydantic import BaseModel

class Metadata(BaseModel):
    workflow: str | None = None
    current_agent: str | None = None