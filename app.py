import streamlit as st

st.title("AI Nutrition Assistant")

user_input = st.text_input("Enter your goal:")

if st.button("Get Advice"):
    st.write("Your diet advice will appear here")
