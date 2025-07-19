# 🎯 Career Path Recommender

This project uses **Machine Learning** to recommend the most suitable **career path** for students based on psychological traits and aptitude scores. It is deployed as an interactive **Streamlit web app**.

---

## 💡 Features

* Predicts career paths like:

  * 🎨 Artist
  * 🧪 Scientist
  * ⚙️ Engineer
  * 🔍 Forensic Psychologist
  * 📚 Writer and more
* Takes input from:

  * **OCEAN Personality Traits** (Big Five Model):

    * Openness, Conscientiousness, Extraversion, Agreeableness, Emotional Stability
  * **Aptitude Scores**:

    * Numerical, Spatial, Abstract, Verbal, Perceptual Reasoning
* Built using:

  * Python 🐍
  * Scikit-learn (RandomForest Classifier)
  * Streamlit (UI)
* Dark Mode UI for better experience

---

## 🚀 Quick Start

### 🔧 Setup

```bash
pip install -r requirements.txt
```

### ▶️ Run Streamlit App

```bash
streamlit run streamlit_app.py
```

---

## 📸 Screenshots

### 🎯 Streamlit App - Career Path Prediction UI

---

### ✅ Predicted Career Output

---

## 📁 Project Structure

```
career_path_recommender/
│
├── data/
│   └── career_data.csv                  # Dataset
│
├── models/
│   └── career_model.pkl                 # Trained ML model
│
├── src/
│   ├── preprocess.py                    # Data preprocessing code
│   ├── predict.py                       # Prediction logic
│   ├── train.py                         # Training script
│   └── main.py                          # Entry-point logic (optional)
│
├── streamlit_app.py                     # Streamlit web app
├── requirements.txt                     # Python dependencies
└── README.md                            # You're here!
```

---

## 🤖 ML Model Info

* **Algorithm**: Random Forest Classifier
* **Training**: Done via `train.py` or button inside Streamlit
* **Target**: Career Label
* **Features**: All OCEAN + Aptitude traits (numeric)

---

## 🧠 How It Works

1. User moves sliders to enter scores.
2. Model predicts best-fit career.
3. Result shown interactively.

---

## 🙌 Credits

Made with ❤️ using Streamlit and Scikit-learn.
Developed as part of an MLOps learning project.
