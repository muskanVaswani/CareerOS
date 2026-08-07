from app.agents.base_agent import BaseAgent
from app.schemas.state.career_state import CareerState
from app.services.career_knowledge_base.service import CareerKnowledgeService
from app.schemas.skill_gap import SkillGap


class SkillGapAgent(BaseAgent):
    
    
    def __init__(self):
        self.career_knowledge_service = CareerKnowledgeService()
        
        
        
    def execute(self, state: CareerState) -> CareerState:
        target_role = state.request.career_goal.target_role
        
        career_profile = self.career_knowledge_service.get_career_profile(target_role.replace(" ","_").lower())
    
    
        # print(career_profile)
        state.context.career_profile = career_profile
        
        if career_profile is None:
            return state
        
        user_skills = set(state.context.profile.skills)
        required_skills = set(career_profile.core_skills)
        
        matched_skills = [skill for skill in career_profile.core_skills
        if skill in user_skills
                          ]
        
        missing_skills = [
            skill for skill in career_profile.core_skills
            if skill not in user_skills
        ]
        
        completion_percentage = (
            len(matched_skills) / len(required_skills))* 100
        
        
        state.results.skill_gap = SkillGap(
            matched_core_skills=matched_skills,
            missing_core_skills=missing_skills,
            knowledge_gaps=career_profile.knowledge_areas,
            missing_tools=career_profile.essential_tools,
            completion_percentage=round(completion_percentage,2)
        )
        
        return state