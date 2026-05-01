import streamlit as st
import google.generativeai as genai
import os

# API key load
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-pro")

st.title("🥗 AI Nutrition Assistant")

# Chat input
user_input = st.text_input("Enter your goal (weight loss, diabetes, etc):")

if st.button("Get Diet Advice"):
    if user_input:
        prompt = f"""
        You are a smart nutrition assistant.

        Give:
        - Indian diet plan
        - budget friendly
        - what to eat
        - what to avoid

        User: {user_input}
        """

        response = model.generate_content(prompt)
        st.write(response.text)
