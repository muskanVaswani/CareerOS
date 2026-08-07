from app.agents.base_agent import BaseAgent
from app.schemas.state.career_state import CareerState

from app.schemas.profile import Profile

class ProfileAgent(BaseAgent):
    def execute(self, state: CareerState)-> CareerState:
        
        state.context.profile = Profile(
            name="Unknown",
            target_role=state.request.career_goal.target_role,
            skills=[
                "python",
                "git",
                "api_development"
            ]
        )
        
        return state