from abc import ABC, abstractmethod

from app.schemas.state.career_state import CareerState


class BaseAgent(ABC):
    
    @abstractmethod
    def execute(self, state: CareerState)-> CareerState:
        pass