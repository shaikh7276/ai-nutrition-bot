import streamlit as st
import google.generativeai as genai

# Page settings
st.set_page_config(
    page_title="AI Nutrition Assistant",
    page_icon="🥗"
)

# Gemini API Key
API_KEY = "PASTE_YOUR_GEMINI_API_KEY_HERE"

# Configure Gemini
genai.configure(api_key=API_KEY)

# Load model
model = genai.GenerativeModel("gemini-2.0-flash")

# App UI
st.title("🥗 AI Nutrition Assistant")
st.write("Get personalized nutrition and diet advice.")

goal = st.text_input(
    "Enter your nutrition goal",
    placeholder="Weight loss, muscle gain, healthy diet..."
)

if st.button("Get Advice"):
    if goal:
        with st.spinner("Generating advice..."):
            prompt = f"""
            You are a certified nutritionist.

            User Goal: {goal}

            Give:
            1. Diet Plan
            2. Foods to Eat
            3. Foods to Avoid
            4. Water Intake
            5. Exercise Tips

            Keep the answer simple.
            """

            try:
                response = model.generate_content(prompt)
                st.success("Advice Generated!")
                st.write(response.text)

            except Exception as e:
                st.error(f"Error: {e}")

    else:
        st.warning("Please enter a goal.")
