# Pima Indians Diabetes Prediction App

This is a web application that predicts whether a patient has diabetes based on diagnostic measurements. It uses a Logistic Regression model trained on the Pima Indians Diabetes Database.

## Project Structure

- `data.py`: Downloads the dataset from Kaggle, cleans it, imputes missing values, scales features, and saves the processed data.
- `train.py`: Loads processed data, trains a Logistic Regression model, and saves the model.
- `predict.py`: Contains the logic to load the model and make predictions on new data.
- `app.py`: A Flask web application that serves a UI for users to input data and get predictions.
- `templates/index.html`: The HTML form for the web interface.
- `Dockerfile`: Configuration to containerize the application.
- `requirements.txt`: List of Python dependencies.

## Setup and Installation

### Local Development

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/FAKER-112/Pima-Indians-Diabetes-Prediction-App.git
    cd Pima-Indians-Diabetes-Prediction-App
    ```

2.  **Create and activate a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

The application requires a sequence of steps to prepare the data and model before serving the app.

1.  **Data Preparation:**
    Download and process the data. This will create a `processed_data` directory.
    ```bash
    python data.py
    ```

2.  **Model Training:**
    Train the model using the processed data. This will create a `models` directory.
    ```bash
    python train.py
    ```

3.  **Run the App:**
    Start the Flask server.
    ```bash
    python app.py
    ```
    Open your browser and navigate to `http://localhost:5000`.

### Docker

You can also run the application using Docker. The Docker image handles the data preparation and training steps automatically upon startup.

1.  **Build the Docker image:**
    ```bash
    docker build -t diabetes-app .
    ```

2.  **Run the container:**
    ```bash
    docker run -p 5000:5000 diabetes-app
    ```
    Access the app at `http://localhost:5000`.

Note: The `data.py` script downloads data from Kaggle. Ensure you have internet access. If authentication is required for `kagglehub` in the future, you may need to pass credentials. Currently, it accesses a public dataset.

### Kubernetes Deployment

To deploy the application to a local Kubernetes cluster using Kind:

#### Option 1: Using Makefile (Recommended)
This automates building, cluster creation, and deployment.
```bash
make run
```
This command will:
1. Build the Docker image.
2. Create a Kind cluster with the correct port mapping.
3. Load the image into the cluster.
4. Deploy the application service.

#### Option 2: Manual Steps
If you don't have `make` installed, run these commands:

1. **Build the image:**
   ```bash
   docker build -t diabetes-app:latest .
   ```

2. **Create Cluster:**
   ```bash
   kind create cluster --config kind-config.yaml
   ```

3. **Load Image:**
   ```bash
   kind load docker-image diabetes-app:latest
   ```

4. **Deploy:**
   ```bash
   kubectl apply -f deployment.yaml
   kubectl apply -f service.yaml
   ```

The app will be accessible at `http://localhost:5000`.
#
