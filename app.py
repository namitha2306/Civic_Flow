import streamlit as st
from workflow import run_workflow

st.set_page_config(page_title="CivicFlow.AI - Citizen Helpdesk", layout="centered")
st.title("🧭 CivicFlow.AI - Citizen Helpdesk (Demo)")

query = st.text_input("Ask a government-related question (e.g., How to renew Aadhaar?)")

if st.button("Get Answer"):
    if not query.strip():
        st.error("Please type a question.")
    else:
        with st.spinner("Processing..."):
            result = run_workflow(query)

        st.subheader("Answer")
        st.write(result.get("final_text", "No answer returned."))

        st.subheader("Sources used")
        for url in result.get("sources", []):
            st.write(f"- {url}")

        # ✅ Move this part INSIDE the button block
        st.subheader("Review Feedback")
        st.json(result.get("review", {}))
