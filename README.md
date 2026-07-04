# CareerOS

> **Your AI Career Operating System**

CareerOS is a **multi-agent AI platform** that helps students, job seekers, and professionals make informed career decisions through personalized AI guidance.

Instead of providing generic advice, CareerOS uses specialized AI agents that collaborate to analyze user profiles, identify skill gaps, generate personalized learning roadmaps, recommend portfolio projects, conduct interview preparation, and provide recruiter-style feedback.

---

## Why CareerOS?

Career growth today is fragmented.

One platform helps you build a resume.

Another suggests courses.

Another provides mock interviews.

Another recommends projects.

CareerOS brings everything together into a single AI-powered career operating system.

---

## Features

### Profile Generation
- Resume parsing
- Questionnaire analysis
- User profile generation

### Skill Intelligence
- Skill extraction
- Skill categorization
- Skill gap analysis

### Personalized Roadmaps
- Learning roadmap generation
- Beginner to advanced progression
- Technology recommendations

### Project Recommendations
- Portfolio project suggestions
- Difficulty-based recommendations
- Resume-focused projects

### Interview Preparation
- AI-generated interview questions
- Technical interview simulation
- Behavioral interview practice

### Recruiter Feedback
- Resume evaluation
- Profile improvement suggestions
- Hiring readiness score

---

## Multi-Agent Architecture

                              +------------------+
                              |      User        |
                              +------------------+
                                        |
                                        |
                              +------------------+
                              |   Frontend (UI)  |
                              +------------------+
                                        |
                                        |
                              +------------------+
                              |  FastAPI Backend |
                              +------------------+
                                        |
                                        |
                              +------------------+
                              | Authentication   |
                              | (JWT / OAuth)    |
                              +------------------+
                                        |
                                        |
                              +------------------+
                              |  API Controller  |
                              +------------------+
                                        |
                                        |
                        +--------------------------------+
                        |     LangGraph Orchestrator     |
                        +--------------------------------+
                                        |
        -----------------------------------------------------------------
        |             |             |             |            |          |
        ▼             ▼             ▼             ▼            ▼          ▼
+---------------+ +---------------+ +---------------+ +---------------+ +---------------+ +----------------+
| Profile Agent | | Skill Agent   | | Roadmap Agent | | Project Agent | | Interview     | | Recruiter      |
|               | |               | |               | |               | | Agent         | | Agent          |
+---------------+ +---------------+ +---------------+ +---------------+ +---------------+ +----------------+
        |              |                |                |                 |                  |
        --------------------------------------------------------------------
                                        |
                                        ▼
                            +-----------------------+
                            | Shared Memory / State |
                            +-----------------------+
                                        |
            ---------------------------------------------------------
            |                     |                    |             |
            ▼                     ▼                    ▼             ▼
+--------------------+  +------------------+  +----------------+ +------------------+
| Prompt Templates   |  | Knowledge Base   |  | Vector DB      | | PostgreSQL       |
|                    |  | (Career Data)    |  | (ChromaDB)     | | User Data        |
+--------------------+  +------------------+  +----------------+ +------------------+
                                        |
                                        ▼
                              +------------------+
                              | LLM Provider     |
                              | OpenAI/Gemini    |
                              | OpenRouter       |
                              +------------------+

Each agent is responsible for a single task while the orchestrator coordinates communication between them.

---

## Tech Stack

### Backend
- Python
- FastAPI

### AI Frameworks
- LangGraph
- LangChain

### LLMs
- OpenAI
- Gemini
- OpenRouter

### Database
- PostgreSQL

### Vector Database
- ChromaDB

### Authentication
- JWT

### Deployment
- Docker

---

## Project Structure

```
CareerOS/

├── backend/
├── agents/
│   ├── profile_agent/
│   ├── skill_agent/
│   ├── roadmap_agent/
│   ├── project_agent/
│   ├── interview_agent/
│   └── recruiter_agent/
│
├── orchestrator/
├── database/
├── prompts/
├── knowledge_base/
├── api/
├── models/
├── tests/
└── README.md
```

---

## Current Development Status

CareerOS is currently under active development.

### Planned Modules

- Resume Parser
- Questionnaire Engine
- Profile Generator
- Skill Gap Analysis
- Personalized Roadmaps
- Project Recommendation Engine
- AI Interviewer
- Recruiter Feedback System
- Career Analytics Dashboard

---

## Future Vision

CareerOS is designed to become a complete AI-powered career operating system capable of supporting multiple career domains through a scalable multi-agent architecture.

Future versions will include:
- Career switching assistance
- Job matching
- Salary insights
- Certification recommendations
- AI portfolio review
- Team collaboration
- Mentor matching

---

## Contributing

Contributions, suggestions, and feedback are welcome.

Feel free to open an issue or submit a pull request.


---

Made with ❤️ to simplify career growth using AI.