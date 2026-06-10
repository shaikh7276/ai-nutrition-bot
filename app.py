import streamlit as st
import google.generativeai as genai

# --------------------
# PAGE CONFIG
# --------------------
st.set_page_config(
    page_title="AI Nutrition Assistant",
    page_icon="🥗",
    layout="wide"
)

# --------------------
# CUSTOM CSS
# --------------------
st.markdown("""
<style>
.main {
    padding-top: 1rem;
}

.metric-box {
    background-color: #f5f7fa;
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    border: 1px solid #e0e0e0;
}

.stButton > button {
    width: 100%;
    height: 50px;
    border-radius: 10px;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

# --------------------
# GEMINI API
# --------------------
API_KEY = st.secrets["AQ.Ab8RN6K2y_ZNN-fMnITA_EIbbPs9NJtNlcY_amEZxEqdgDPLLg"]

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")

# --------------------
# SIDEBAR
# --------------------
with st.sidebar:
    st.title("🥗 Nutrition Bot")

    age = st.number_input("Age", 15, 100, 21)
    weight = st.number_input("Weight (kg)", 30, 200, 70)
    height = st.number_input("Height (cm)", 100, 250, 170)

    goal = st.selectbox(
        "Goal",
        [
            "Weight Loss",
            "Muscle Gain",
            "Healthy Diet",
            "Fat Loss"
        ]
    )

# --------------------
# HEADER
# --------------------
st.title("🥗 AI Nutrition Assistant")
st.caption("Your Personal AI Diet & Fitness Coach")

# --------------------
# BMI
# --------------------
bmi = weight / ((height / 100) ** 2)

if bmi < 18.5:
    status = "Underweight"
elif bmi < 25:
    status = "Normal"
elif bmi < 30:
    status = "Overweight"
else:
    status = "Obese"

# --------------------
# DASHBOARD
# --------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("BMI", f"{bmi:.1f}")

with col2:
    st.metric("Weight", f"{weight} kg")

with col3:
    st.metric("Status", status)

st.divider()

# --------------------
# TABS
# --------------------
tab1, tab2 = st.tabs(["🍽 Diet Plan", "📊 Health Info"])

with tab1:

    st.subheader("Generate AI Diet Plan")

    if st.button("🚀 Generate Diet Plan"):
        prompt = f"""
        Create a nutrition and diet plan.

        Age: {age}
        Weight: {weight} kg
        Height: {height} cm
        Goal: {goal}

        Include:
        - Breakfast
        - Lunch
        - Dinner
        - Snacks
        - Water intake
        - Exercise tips

        Keep it practical.
        """

        with st.spinner("Generating plan..."):
            response = model.generate_content(prompt)

        st.success("Diet Plan Ready")
        st.write(response.text)

with tab2:

    st.subheader("Health Summary")

    st.write(f"**Age:** {age}")
    st.write(f"**Height:** {height} cm")
    st.write(f"**Weight:** {weight} kg")
    st.write(f"**BMI:** {bmi:.1f}")
    st.write(f"**Goal:** {goal}")

    st.info(
        "This AI assistant provides general nutrition guidance and is not a substitute for professional medical advice."
    )
