import streamlit as st # type: ignore
import requests

st.title("HR AI Chatbot")

query = st.text_input("Enter your HR-related question:")

top_k = st.slider("Number of results to fetch", 1, 5, 3)

if st.button("Ask"):
    if not query.strip():
        st.warning("Please enter a query.")
    else:
        with st.spinner("Fetching answers..."):
            try:
                response = requests.post(
                    "http://backend:8000/chat",
                    json={"query": query, "top_k": top_k},
                    timeout=10,
                )
                response.raise_for_status()
                data = response.json()

                st.markdown(f"**Answer:** {data['answer']}")

                st.markdown("### Candidate Matches:")
                for c in data['candidates']:
                    st.markdown(
                        f"- **{c['name']}** ({c['experience_years']} yrs) — Skills: {', '.join(c['skills'])} — Availability: {c['availability']} — Similarity: {c['similarity_score']:.2f}"
                    )
            except Exception as e:
                st.error(f"Error: {e}")
