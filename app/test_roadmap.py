import json

from app.prompts.roadmap_prompt import build_roadmap_prompt
from app.schemas.roadmap import Roadmap
from app.services.llm.ollama_service import OllamaService


llm = OllamaService()

prompt = """
You are the Roadmap Agent of CareerOS.

Create a SHORT learning roadmap for an AI Engineer.

The user currently knows:
- Python
- Git
- API Development

The user needs to learn:
- Machine Learning
- Deep Learning
- Large Language Models

Available time:
2 hours per week

Target duration:
2 weeks

Return ONLY valid JSON.

The JSON MUST have exactly these top-level fields:
- goal
- depth
- phases

The phases field must be a list.

Each phase MUST contain:
- phase
- title
- topics
- depth
- estimated_weeks
- project

Do not add a "roadmap" wrapper.
Do not add explanations.
Keep the roadmap to a maximum of 2 phases.
"""

print("Generating roadmap...")

response = llm.generate(
    prompt,
    format="json"
)

print("RAW RESPONSE:")
print(response)

roadmap_data = json.loads(response)

roadmap = Roadmap.model_validate(roadmap_data)

print("\nVALIDATED ROADMAP:")
print(roadmap)