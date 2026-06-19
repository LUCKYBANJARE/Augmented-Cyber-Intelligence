import streamlit as st
from planner import create_plan
from executor import execute_step

st.title("🧠 Multi-Step AI Agent")

user_input = st.text_input("Enter your task:")

if st.button("Run Agent"):
    plan = create_plan(user_input)
    steps = plan.get("steps", [])

    context = ""

    for i, step in enumerate(steps, 1):
        st.subheader(f"Step {i}: {step}")

        result = execute_step(step, context)
        st.write(result)

        context += f"\nStep {i}: {result}"