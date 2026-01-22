import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def train_model():
    # Define directories
    output_dir = 'processed_data'
    models_dir = 'models'
    os.makedirs(models_dir, exist_ok=True)

    # 1. Load preprocessed data and scaler
    print("Loading preprocessed data...")
    X_path = os.path.join(output_dir, 'X_preprocessed.csv')
    y_path = os.path.join(output_dir, 'y_target.csv')
    scaler_path = os.path.join(output_dir, 'scaler.pkl')

    X = pd.read_csv(X_path)
    y = pd.read_csv(y_path).squeeze() # .squeeze() to convert DataFrame to Series
    scaler = joblib.load(scaler_path)
    print("Preprocessed data and scaler loaded successfully.")

    # 2. Split the dataset into training and testing sets
    print("Splitting data into training and testing sets...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print(f"Training data shape: {X_train.shape}, {y_train.shape}")
    print(f"Testing data shape: {X_test.shape}, {y_test.shape}")

    # 3. Instantiate and train Logistic Regression model with best hyperparameters
    print("Training Logistic Regression model...")
    model = LogisticRegression(C=1, solver='liblinear', random_state=42)
    model.fit(X_train, y_train)
    print("Logistic Regression model trained successfully.")

    # 4. Save the trained model
    model_path = os.path.join(models_dir, 'logistic_regression_model.pkl')
    joblib.dump(model, model_path)
    print(f"Trained Logistic Regression model saved to {model_path}")

    print("Model training script finished.")

if __name__ == '__main__':
    train_model()
