import os
import json
import pickle
from typing import List, Dict

INDEX_DIR = "index"

def employee_to_text(emp: Dict) -> str:
    return f"{emp.get('name','')}. Skills: {', '.join(emp.get('skills',[]))}. Experience: {emp.get('experience_years',0)} years. Projects: {'. '.join(emp.get('past_projects',[]))}. Availability: {emp.get('availability','')}."

def build_index(employees: List[Dict]):
    """Mock index builder: just save employee data without embeddings."""
    os.makedirs(INDEX_DIR, exist_ok=True)
    with open(os.path.join(INDEX_DIR, "meta.pkl"), "wb") as f:
        pickle.dump({"employees": employees}, f)

def load_index():
    """Load employee data from the mock index."""
    meta_path = os.path.join(INDEX_DIR, "meta.pkl")
    if not os.path.exists(meta_path):
        return None, None, None
    with open(meta_path, "rb") as f:
        meta = pickle.load(f)
    return None, meta, None  

def query_semantic(query: str, top_k: int = 5, index=None, meta=None, model=None):
    """Simple keyword-based search without embeddings."""
    if meta is None:
        raise ValueError("Meta must be provided")

    employees = meta["employees"]
    results = []
    for emp in employees:
        text = employee_to_text(emp).lower()
        score = text.count(query.lower())
        if score > 0:
            emp_copy = emp.copy()
            emp_copy["similarity_score"] = float(score)
            results.append(emp_copy)

    # Sort by score descending and limit to top_k
    return sorted(results, key=lambda e: e["similarity_score"], reverse=True)[:top_k]
