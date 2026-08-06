from app.services.career_knowledge_base.local_provider import LocalProvider

provider = LocalProvider()

career = provider.get_career_profile("ai_engineer")
print(career)