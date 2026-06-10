import streamlit as st
import google.generativeai as genai

# Page Config
st.set_page_config(
    page_title="AI Nutrition Assistant",
    page_icon="🥗"
)

st.title("🥗 AI Nutrition Assistant")
st.write("Get personalized nutrition and diet advice.")

# Configure Gemini API
try:
    api_key = st.secrets["AQ.Ab8RN6Lpwso-SbCHk9VnIdyunq3PKCQ59U0hRo1BI0P-F3hHQA"]
    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("gemini-2.0-flash")

    goal = st.text_input(
        "What is your nutrition goal?",
        placeholder="Example: Weight loss, muscle gain, healthy diet..."
    )

    if st.button("Get Advice"):
        if goal.strip():
            with st.spinner("Generating nutrition advice..."):
                prompt = f"""
                You are a professional nutritionist.

                User Goal: {goal}

                Provide:
                1. Diet recommendation
                2. Foods to eat
                3. Foods to avoid
                4. Daily nutrition tips
                5. Water intake recommendation

                Keep the answer simple and practical.
                """

                response = model.generate_content(prompt)

                st.success("Advice Generated!")
                st.write(response.text)

        else:
            st.warning("Please enter your goal.")

except Exception as e:
    st.error(f"Error: {e}")
