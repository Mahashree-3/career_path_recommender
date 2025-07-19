import joblib
import pandas as pd
import os

def predict_from_input(user_input):
    model_path = 'models/career_model.pkl'
    
    if not os.path.exists(model_path):
        raise FileNotFoundError("Model not found. Please run train_model() first.")

    # Load model
    model = joblib.load(model_path)

    # Convert user input to DataFrame
    input_df = pd.DataFrame([user_input])

    # Predict
    prediction = model.predict(input_df)

    return prediction[0]
