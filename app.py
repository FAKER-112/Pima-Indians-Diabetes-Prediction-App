from flask import Flask, request, render_template
import os
import sys

# Add the current directory to the path to import predict.py
sys.path.append(os.path.dirname(__file__))
from predict import predict_outcome

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction_text = None
    if request.method == 'POST':
        try:
            # Get form data
            input_data = {
                'Pregnancies': int(request.form['Pregnancies']),
                'Glucose': float(request.form['Glucose']),
                'BloodPressure': float(request.form['BloodPressure']),
                'SkinThickness': float(request.form['SkinThickness']),
                'Insulin': float(request.form['Insulin']),
                'BMI': float(request.form['BMI']),
                'DiabetesPedigreeFunction': float(request.form['DiabetesPedigreeFunction']),
                'Age': int(request.form['Age'])
            }

            # Make prediction
            prediction = predict_outcome(input_data)

            if prediction is not None:
                if prediction == 1:
                    prediction_text = "Predicted Outcome: Diabetic (1)"
                else:
                    prediction_text = "Predicted Outcome: Non-Diabetic (0)"
            else:
                prediction_text = "Error during prediction. Check server logs."

        except Exception as e:
            prediction_text = f"Error processing input: {e}"

    # Render the HTML template, passing the prediction text if available
    return render_template('index.html', prediction_text=prediction_text)

if __name__ == '__main__':
    # Create necessary directories if they don't exist
    os.makedirs('processed_data', exist_ok=True)
    os.makedirs('models', exist_ok=True)
    print("Ensure 'processed_data/scaler.pkl' and 'models/logistic_regression_model.pkl' exist.")
    print("Run 'python data.py' and 'python train.py' first.")
    app.run(debug=True, host='0.0.0.0', port=5000)
