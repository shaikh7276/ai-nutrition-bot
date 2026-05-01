import streamlit as st
import google.generativeai as genai
import os

# API key
api_key = os.getenv("AIzaSyAb5s0dTp12BOOqtYaHEscLMJ1_b0KLKQE")
genai.configure(api_key=api_key)

# Updated model
model = genai.GenerativeModel("gemini-1.5-flash")

st.title("🥗 AI Nutrition Assistant")

user_input = st.text_input("Enter your goal:")

if st.button("Get Advice"):
    if user_input:
        prompt = f"""
        You are a nutrition assistant.
        Give simple Indian diet plan, budget friendly.

        User: {user_input}
        """

        response = model.generate_content(prompt)
        st.write(response.text)
