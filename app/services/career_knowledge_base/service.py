from app.schemas.career_profile import CareerProfile
from app.services.career_knowledge_base.local_provider import LocalProvider


class CareerKnowledgeService:
    
    def __init__(self):
        self.local_provider = LocalProvider()
        
        
    def get_career_profile(self, role: str)-> CareerProfile | None:
        return self.local_provider.get_career_profile(role)
    
    