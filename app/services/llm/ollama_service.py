import requests

from app.services.llm.service import LLMService


class OllamaService(LLMService):
    
    def __init__(self,model: str = "qwen3:4b"):
        self.model = model
        self.base_url = "http://localhost:11434"
        
    
    def generate(self, prompt: str, format: str| None = None) -> str:
        
        response = requests.post(
            f"{self.base_url}/api/generate",
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False,
                "format": format,
                "think": False
                }
        )
        
        
        response.raise_for_status()
        
        # print("STATUS:", response.status_code)
        # print("RAW OLLAMA RESPONSE:", response.text)
        
        return response.json()["response"]