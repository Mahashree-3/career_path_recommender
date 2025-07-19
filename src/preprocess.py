import pandas as pd
from sklearn.model_selection import train_test_split

def load_and_preprocess_data():
    # Load the dataset
    df = pd.read_csv('data/career_prediction.csv')

    # Drop any rows with missing values
    df = df.dropna()

    # Separate features and target
    X = df.drop('Suggested Job Role', axis=1)
    y = df['Suggested Job Role']

    # Convert categorical features to numbers (if any)
    X = pd.get_dummies(X, drop_first=True)

    # Encode target labels into numbers
    from sklearn.preprocessing import LabelEncoder
    le = LabelEncoder()
    y = le.fit_transform(y)

    # Split into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test, le
