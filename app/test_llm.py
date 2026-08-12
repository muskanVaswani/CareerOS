from app.services.llm.ollama_service import OllamaService


llm = OllamaService()


response = llm.generate(
    "Explain what machine learning is in two simple sentences."
)

print(response)