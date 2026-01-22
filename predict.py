import pandas as pd
import joblib
import os
import numpy as np # Import numpy for potential future use or consistency

def predict_outcome(input_data):
    # Define directories
    output_dir = 'processed_data'
    models_dir = 'models'

    # Check if artifacts exist
    scaler_path = os.path.join(output_dir, 'scaler.pkl')
    model_path = os.path.join(models_dir, 'logistic_regression_model.pkl')

    if not os.path.exists(scaler_path):
        print(f"Error: Scaler not found at {scaler_path}. Please run data.py and train.py first.")
        return None
    if not os.path.exists(model_path):
        print(f"Error: Model not found at {model_path}. Please run data.py and train.py first.")
        return None

    # 1. Load the StandardScaler and the trained Logistic Regression model
    print("Loading StandardScaler and trained model...")
    scaler = joblib.load(scaler_path)
    model = joblib.load(model_path)
    print("StandardScaler and model loaded successfully.")

    # 2. Convert input_data dictionary into a pandas DataFrame
    # Ensure column order matches the training data
    feature_names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
    input_df = pd.DataFrame([input_data], columns=feature_names)
    print("Input data converted to DataFrame.")

    # 3. Scale the input data using the loaded StandardScaler
    print("Scaling input data...")
    scaled_input_data = scaler.transform(input_df)
    print("Input data scaled.")

    # 4. Use the loaded model to make a prediction
    prediction = model.predict(scaled_input_data)

    # 5. Return the prediction
    return prediction[0]

if __name__ == '__main__':
    # Example usage:
    print("\n--- Testing predict.py with sample data ---")
    # Sample input data for a non-diabetic individual (based on typical ranges)
    sample_non_diabetic = {
        'Pregnancies': 1,
        'Glucose': 100,
        'BloodPressure': 70,
        'SkinThickness': 20,
        'Insulin': 80,
        'BMI': 25.0,
        'DiabetesPedigreeFunction': 0.3,
        'Age': 25
    }
    predicted_class_non_diabetic = predict_outcome(sample_non_diabetic)
    if predicted_class_non_diabetic is not None:
        print(f"Sample Non-Diabetic Input: {sample_non_diabetic}")
        print(f"Predicted Outcome (0: Non-Diabetic, 1: Diabetic): {predicted_class_non_diabetic}")

    print("\n")

    # Sample input data for a potentially diabetic individual (based on typical ranges)
    sample_diabetic = {
        'Pregnancies': 6,
        'Glucose': 150,
        'BloodPressure': 80,
        'SkinThickness': 35,
        'Insulin': 150,
        'BMI': 35.0,
        'DiabetesPedigreeFunction': 0.7,
        'Age': 50
    }
    predicted_class_diabetic = predict_outcome(sample_diabetic)
    if predicted_class_diabetic is not None:
        print(f"Sample Diabetic Input: {sample_diabetic}")
        print(f"Predicted Outcome (0: Non-Diabetic, 1: Diabetic): {predicted_class_diabetic}")

    print("\nPrediction script finished.")
