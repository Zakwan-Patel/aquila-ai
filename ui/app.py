import streamlit as st
import requests

st.set_page_config(
    page_title="Aquila AI",
    page_icon="🦅",
    layout="centered"
)

st.title("🦅 Aquila AI")
st.subheader("Enterprise Knowledge & Decision Assistant")

st.markdown(
    """
Ask questions based on internal documents.
Answers are **grounded**, **verified**, and **source-backed**.
"""
)

API_URL = "http://127.0.0.1:8000/rag/ask"

question = st.text_input("Enter your question:")

if st.button("Ask"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            response = requests.post(
                API_URL,
                json={"question": question},
                timeout=30
            )

        if response.status_code == 200:
            data = response.json()

            st.markdown("### ✅ Answer")
            st.write(data["answer"])

            st.markdown("### 🔎 Verification")
            if data["verified"]:
                st.success("Verified against source documents")
            else:
                st.error("Could not verify answer")

            st.markdown("### 📄 Sources")
            for src in data.get("sources", []):
                st.write(f"- {src}")
        else:
            st.error("API error. Please try again.")
