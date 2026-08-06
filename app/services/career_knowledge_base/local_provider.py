from app.schemas.career_profile import CareerProfile
import json
from pathlib import Path


class LocalProvider:
    
    def __init__(self):
        self.data_file = (
            Path(__file__).resolve().parents[3]
            / "data"
            / "careers"
            / "career_knowledge.json"
        )


    
    def get_career_profile(self,role:str) -> CareerProfile | None:
        with open(self.data_file, "r", encoding="utf-8") as file:
            careers = json.load(file)
            
        for career in careers:
            if career["id"] == role:
                return CareerProfile(**career)
            
        return None