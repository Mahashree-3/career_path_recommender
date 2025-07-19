import streamlit as st
import pandas as pd
import pickle
import os

st.set_page_config(page_title="Career Path Recommender", layout="wide")
st.sidebar.title("Career Path Recommender")

# 🔁 Train Model
if st.sidebar.button("📄 Train Model"):
    data = pd.read_csv("data/career_data.csv")
    X = data.drop("Career", axis=1)
    y = data["Career"]

    from sklearn.ensemble import RandomForestClassifier
    model = RandomForestClassifier()
    model.fit(X, y)

    os.makedirs("models", exist_ok=True)
    with open("models/career_model.pkl", "wb") as f:
        pickle.dump(model, f)

    st.sidebar.success("Model trained and saved!")

# 🎯 Prediction Section
st.title("🎯 Career Path Prediction")

st.markdown("Enter your scores below to get your predicted career path:")

# Collect 10 input features
col1, col2, col3 = st.columns(3)

with col1:
    O_score = st.slider("Openness Score (O)", 0.0, 10.0, 5.0)
    E_score = st.slider("Extraversion Score (E)", 0.0, 10.0, 5.0)
    Numerical = st.slider("Numerical Aptitude", 0.0, 10.0, 5.0)
    Abstract = st.slider("Abstract Reasoning", 0.0, 10.0, 5.0)

with col2:
    C_score = st.slider("Conscientiousness Score (C)", 0.0, 10.0, 5.0)
    A_score = st.slider("Agreeableness Score (A)", 0.0, 10.0, 5.0)
    Spatial = st.slider("Spatial Aptitude", 0.0, 10.0, 5.0)
    Verbal = st.slider("Verbal Reasoning", 0.0, 10.0, 5.0)

with col3:
    E_score_2 = st.slider("Emotional Stability (N)", 0.0, 10.0, 5.0)
    Perceptual = st.slider("Perceptual Aptitude", 0.0, 10.0, 5.0)

if st.button("🔮 Predict Career Path"):
    try:
        with open("models/career_model.pkl", "rb") as f:
            model = pickle.load(f)

        input_data = pd.DataFrame([[
            O_score, C_score, E_score, A_score, E_score_2,
            Numerical, Spatial, Perceptual, Abstract, Verbal
        ]], columns=[
            'O_score', 'C_score', 'E_score', 'A_score', 'N_score',
            'Numerical Aptitude', 'Spatial Aptitude',
            'Perceptual Aptitude', 'Abstract Reasoning',
            'Verbal Reasoning'
        ])

        prediction = model.predict(input_data)[0]
        st.success(f"🎓 Recommended Career Path: **{prediction}**")
    except Exception as e:
        st.error("⚠️ Failed to load model or predict.")
        st.exception(e)