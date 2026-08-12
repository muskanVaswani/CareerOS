import json

from app.agents.base_agent import BaseAgent
from app.schemas.state.career_state import CareerState
from app.services.llm.ollama_service import OllamaService
from app.prompts.roadmap_prompt import build_roadmap_prompt
from app.schemas.roadmap import Roadmap



class RoadmapAgent(BaseAgent):
    
    def __init__(self):
        self.llm = OllamaService()
        
        
        
    def execute(self,state: CareerState)-> CareerState:
        
        skill_gap = state.results.skill_gap
        career_profile = state.context.career_profile
        profile = state.context.profile
        learning_preferences = state.request.learning_preferences
        
        prompt = build_roadmap_prompt(
            career_profile=career_profile,
            profile=profile,
            skill_gap=skill_gap,
            learning_preferences=learning_preferences
        )
        
        response = self.llm.generate(
            prompt,
            format="json"
        )
        print("ROADMAP LLM RESPONSE:")
        print(response)
        
        roadmap_data = json.loads(response)
        roadmap = Roadmap.model_validate(roadmap_data)
        state.results.roadmap = roadmap
        
        
        return state