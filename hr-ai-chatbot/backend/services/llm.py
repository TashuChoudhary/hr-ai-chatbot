from typing import List, Dict

def generate_answer(query: str, hits: List[Dict]) -> str:
    if not hits:
        return f"I couldn't find any employees matching: \"{query}\"."

    lines = [f"Based on your request: \"{query}\", here are the top {len(hits)} matches:"]
    for i, h in enumerate(hits, 1):
        lines.append(f"{i}. {h['name']} — {h.get('experience_years','N/A')} yrs — Skills: {', '.join(h.get('skills',[]))} — Availability: {h.get('availability','unknown')}")
        if h.get("past_projects"):
            lines.append(f"    Projects: {', '.join(h['past_projects'][:3])}")
    lines.append("\nWould you like more details on any candidate or to schedule a call?")
    return "\n".join(lines)