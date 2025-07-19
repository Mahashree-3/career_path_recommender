import streamlit as st
import pandas as pd
from src.predict import predict_from_input

st.title("🎓 Career Path Recommender")

st.markdown("Enter your details to get your recommended career path:")

# Inputs
math = st.slider("Math Score", 0, 100, 50)
reading = st.slider("Reading Score", 0, 100, 50)
science = st.slider("Science Score", 0, 100, 50)

tech = st.slider("Interest in Technology", 0, 10, 5)
bio = st.slider("Interest in Biology", 0, 10, 5)
arts = st.slider("Interest in Arts", 0, 10, 5)
business = st.slider("Interest in Business", 0, 10, 5)

income_priority = st.selectbox("Income Priority", [0, 1, 2])
travel_priority = st.selectbox("Travel Priority", [0, 1, 2])

if st.button("🔍 Predict Career Path"):
    input_data = {
        'math_score': math,
        'reading_score': reading,
        'science_score': science,
        'interest_tech': tech,
        'interest_biology': bio,
        'interest_arts': arts,
        'interest_business': business,
        'income_priority': income_priority,
        'travel_priority': travel_priority
    }

    result = predict_from_input(input_data)
    st.success(f"✅ Recommended Career Path: **{result}**")
