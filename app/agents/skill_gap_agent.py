from app.agents.base_agent import BaseAgent
from app.schemas.state.career_state import CareerState
from app.services.career_knowledge_base.service import CareerKnowledgeService



class SkillGapAgent(BaseAgent):
    
    
    def __init__(self):
        self.career_knowledge_service = CareerKnowledgeService()
        
        
        
    def execute(self, state: CareerState) -> CareerState:
        target_role = state.request.career_goal.target_role
        
        career_profile = self.career_knowledge_service.get_career_profile(target_role.replace(" ","_").lower())
    
    
        # print(career_profile)
        state.context.career_profile = career_profile
        
        return state