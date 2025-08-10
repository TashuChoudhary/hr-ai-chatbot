from fastapi import FastAPI, HTTPException, Query 
from pydantic import BaseModel 
from typing import List
import json

app = FastAPI(
    title="HR AI Chatbot",
    description="AI-powered HR resource query chatbot"
)

# Load employees
with open("data/employees.json", "r") as f:
    employees = json.load(f)

# Request schema
class ChatRequest(BaseModel):
    query: str
    top_k: int = 3

class EmployeeResponse(BaseModel):
    name: str
    skills: List[str]
    experience_years: int
    projects: List[str]
    availability: str
    similarity_score: float

class ChatResponse(BaseModel):
    query: str
    answer: str
    candidates: List[EmployeeResponse]

def mock_query_semantic(query: str, top_k: int):
    # Very simple keyword match for demo
    results = []
    for emp in employees:
        score = sum(query.lower() in s.lower() for s in emp["skills"])
        if score > 0:
            emp_copy = emp.copy()
            emp_copy["similarity_score"] = float(score)
            results.append(emp_copy)
    return sorted(results, key=lambda x: x["similarity_score"], reverse=True)[:top_k]

def mock_generate_answer(query: str, hits: List[dict]):
    if not hits:
        return "No matching employees found."
    names = [emp["name"] for emp in hits]
    return f"Based on your query '{query}', here are some matching employees: {', '.join(names)}."

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(req: ChatRequest):
    query = req.query.strip()
    if not query:
        raise HTTPException(status_code=400, detail="Query cannot be empty.")

    hits = mock_query_semantic(query, req.top_k)
    if not hits:
        raise HTTPException(status_code=404, detail="No matching employees found.")

    answer = mock_generate_answer(query, hits)

    return ChatResponse(query=query, answer=answer, candidates=hits)

@app.get("/employees/search", response_model=List[EmployeeResponse])
async def employee_search(q: str = Query(..., min_length=1)):
    query_lower = q.lower()
    results = []
    for emp in employees:
        # Simple search over skills and name
        if (query_lower in emp.get("name", "").lower() or
            any(query_lower in skill.lower() for skill in emp.get("skills", []))):
            emp_copy = emp.copy()
            emp_copy["similarity_score"] = 0.0  # no semantic score here
            results.append(emp_copy)
    if not results:
        raise HTTPException(status_code=404, detail="No employees found matching the query.")
    return results

 @app.get("/")
async def root():
    return {"status": "backend is running"}

