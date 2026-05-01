import streamlit as st
import google.generativeai as genai
import os

api_key = os.getenv("AIzaSyAb5s0dTp12BOOqtYaHEscLMJ1_b0KLKQE")

if not api_key:
    st.error("API key missing")
else:
    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("models/gemini-1.5-flash")

    st.title("🥗 AI Nutrition Assistant")

    user_input = st.text_input("Enter your goal:")

    if st.button("Get Advice"):
        if user_input:
            try:
                response = model.generate_content(user_input)
                st.write(response.text)
            except Exception as e:
                st.error(str(e))
