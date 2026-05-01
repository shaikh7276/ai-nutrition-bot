import streamlit as st
import os
from google import genai

st.title("🥗 AI Nutrition Assistant")

# Load API key
api_key = os.getenv("AIzaSyAb5s0dTp12BOOqtYaHEscLMJ1_b0KLKQE")

if not api_key:
    st.error("API key missing")
else:
    try:
        client = genai.Client(api_key=api_key)

        user_input = st.text_input("Enter your goal:")

        if st.button("Get Advice"):
            if user_input:
                response = client.models.generate_content(
                    model="gemini-1.0-pro",
                    contents=user_input
                )
                st.write(response.text)

    except Exception as e:
        st.error(f"Error: {e}")

