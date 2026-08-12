import json


from app.services.llm.ollama_service import OllamaService
from app.schemas.roadmap import Roadmap

llm = OllamaService()

prompt = """

Create a simple learning roadmap for someone who wants to learn python.

Return ONLY valid JSON in exactly this structure:

{
    
    "goal": "Python",
    "depth": "basic",
    "phases":[
        {
            
            "phase":1,
            "title":"Python fundamentals",
            "topics": [
                "variables",
                "data types",
                "functions"
            ],
            "depth": "basic",
            "estimated_weeks":2,
            "project": "Build a simple calculator"
            
        }
    ]
    
    }



"""


response = llm.generate(
    prompt,
    format="json"
)


roadmap_data = json.loads(response)
roadmap = Roadmap.model_validate(roadmap_data)

print(roadmap)