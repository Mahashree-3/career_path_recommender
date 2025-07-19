import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
import os

def train_model():
    # Load dataset
    data = pd.read_csv("data/career_data.csv")  # Make sure file name is correct

    # Fix column name to match the actual header
    X = data.drop("Career", axis=1)
    y = data["Career"]

    # Train model
    model = RandomForestClassifier()
    model.fit(X, y)

    # Create 'models' folder if not exists
    os.makedirs("models", exist_ok=True)

    # Save model as pickle file
    with open("models/career_model.pkl", "wb") as f:
        pickle.dump(model, f)
