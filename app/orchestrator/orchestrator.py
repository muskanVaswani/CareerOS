from app.agents.profile_agent import ProfileAgent
from app.schemas.state.career_state import CareerState
from app.schemas.career_goal import CareerGoal
from app.schemas.learning_preferences import LearningPreferences
from app.schemas.state.request import Request


class Orchestrator:
    def __init__(self):
        self.profile_agent = ProfileAgent()
        
    def run(self, user_input: str):
        career_goal = CareerGoal(
            target_role=user_input
            )
        
        learning_preferences = LearningPreferences()
        
        request = Request(
            career_goal=career_goal,
            learning_preferences=learning_preferences
        )
        
        state = CareerState(
            request=request
        )
        
        state.metadata.workflow = "career_analysis"
        state.metadata.current_agent = "ProfileAgent"
        
        
        state = self.profile_agent.execute(state)
        
        return state