import streamlit as st
import os

st.title("🥗 AI Nutrition Assistant")

api_key = os.getenv("AIzaSyAb5s0dTp12BOOqtYaHEscLMJ1_b0KLKQE")

if not api_key:
    st.error("API key missing")
else:
    genai.configure(api_key=api_key)

    user_input = st.text_input("Enter your goal:")

    if st.button("Get Advice"):
        if user_input:
            try:
                response = genai.generate_text(
                    model="models/text-bison-001",
                    prompt=user_input
                )
                st.write(response.result)
            except Exception as e:
                st.error(str(e))
