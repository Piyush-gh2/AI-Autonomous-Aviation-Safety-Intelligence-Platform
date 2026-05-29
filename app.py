import streamlit as st

from src.agents import run_aviation_ai
from src.rag import load_knowledge, build_index, retrieve

st.title("✈️ AI Autonomous Aviation Safety Intelligence Platform")

query = st.text_input("Ask Aviation Intelligence Insight")

if st.button("Analyze Aviation Operations"):

    df, prediction, risk, explanation = run_aviation_ai()

    st.subheader("📊 Aviation Dataset")
    st.dataframe(df)

    st.subheader("📈 Aviation Risk Forecast")
    st.write(f"Predicted Aviation Risk Score: {prediction:.2f}")

    st.subheader("⚠️ Aviation Safety Detection")
    st.write(risk)

    st.subheader("🧠 Explainable AI Insight")
    st.write(explanation)

    st.line_chart(df["engine_temp"])

    # RAG
    docs = load_knowledge()
    index = build_index(docs)

    if query:

        insights = retrieve(query, docs, index)

        st.subheader("🔎 Aviation Intelligence Insights")

        for i in insights:
            st.write(i)