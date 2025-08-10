from typing import List, Optional
from pydantic import BaseModel # type: ignore

class Employee(BaseModel):
    id: Optional[int]
    name: str
    skills: List[str]
    experience_years: int
    past_projects: List[str]
    availability: str

class QueryRequest(BaseModel):
    query: str
