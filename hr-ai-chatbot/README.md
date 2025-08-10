## HR Resource Query Chatbot

## Overview
This project is an AI-powered HR chatbot designed to help users query employee data and get relevant recommendations. It combines a FastAPI backend with a Streamlit frontend, using simple semantic matching for demo purposes.

## Features
- Natural language query input for HR-related questions
- Semantic search over employee skills and profiles
- Candidate match listing with similarity scores
- Simple REST API for querying employees
- Interactive frontend UI with Streamlit

## Architecture
- **Backend:** FastAPI app serving `/chat` endpoint
- **Frontend:** Streamlit app providing user interface
- **Data:** Employee profiles loaded from JSON
- **Deployment:** Docker Compose orchestrating backend and frontend services

## Setup & Installation
1. Clone the repo:
   ```bash
   git clone <repo-url>
   cd hr-ai-chatbot
2. Build and start services:
   docker-compose up --build

''Access frontend at http://localhost:8501 and backend API at http://localhost:8000.

## AI Development Process

    Used ChatGPT and GitHub Copilot extensively for code generation and debugging.

    AI helped generate API schemas, request handling, and frontend logic.

    Approximately 70% of code was AI-assisted.

    AI suggested architectural design choices and error handling improvements.

    Debugged container and deployment issues manually.

## Technical Decisions

    Chose FastAPI for quick, async backend development.

    Used Streamlit for rapid frontend prototyping.

    Opted for local JSON data store for simplicity; scalable DB can be added later.

    Used Docker Compose for easy multi-service orchestration.

    Selected OpenAI ChatGPT for coding help; local LLMs can be explored for privacy.

## Future Improvements

    Integrate real semantic search with embeddings.

    Add user authentication and authorization.

    Migrate data store to a database.

    Deploy on cloud infrastructure with CI/CD pipelines.

    Enhance frontend UI/UX with advanced visualizations.

'' Prepared by Tashu 