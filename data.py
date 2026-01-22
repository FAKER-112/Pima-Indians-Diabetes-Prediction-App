import kagglehub
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import joblib
import os

def download_dataset(dataset_name="uciml/pima-indians-diabetes-database"):
    """Downloads the specified Kaggle dataset and returns its local path."""
    print(f"Downloading dataset: {dataset_name}")
    path = kagglehub.dataset_download(dataset_name)
    print(f"Dataset downloaded to: {path}")
    return path

def load_data(path, filename="diabetes.csv"):
    """Loads the dataset into a pandas DataFrame."""
    df = pd.read_csv(os.path.join(path, filename))
    print("Data loaded successfully.")
    return df

def impute_missing_values(df):
    """Replaces medically implausible zero values with NaN and then imputes NaNs with median."""
    df_copy = df.copy()
    columns_with_zero_as_missing = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']

    # Replace 0 values with NaN in the identified columns
    for col in columns_with_zero_as_missing:
        df_copy[col] = df_copy[col].replace(0, np.nan)

    # Median imputation for missing values
    print("Performing median imputation for missing values...")
    for col in columns_with_zero_as_missing:
        median_value = df_copy[col].median()
        df_copy[col] = df_copy[col].fillna(median_value)
        print(f"  Column '{col}': NaN values imputed with median {median_value:.2f}")

    print("Missing value imputation complete.")
    return df_copy

def scale_features(X):
    """Scales numerical features using StandardScaler and returns the scaled data and the fitted scaler."""
    print("Scaling numerical features using StandardScaler...")
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    X_scaled_df = pd.DataFrame(X_scaled, columns=X.columns, index=X.index)
    print("Feature scaling complete.")
    return X_scaled_df, scaler

def main():
    # 1. Download dataset
    dataset_path = download_dataset()

    # 2. Load data
    df = load_data(dataset_path)

    # 3. Impute missing values
    df_imputed = impute_missing_values(df)

    # 4. Separate features (X) and target (y)
    X = df_imputed.drop('Outcome', axis=1)
    y = df_imputed['Outcome']
    print(f"Features (X) shape: {X.shape}")
    print(f"Target (y) shape: {y.shape}")

    # 5. Scale features
    X_scaled, scaler = scale_features(X)

    # 6. Save preprocessed data and scaler
    output_dir = 'processed_data'
    os.makedirs(output_dir, exist_ok=True)

    X_scaled.to_csv(os.path.join(output_dir, 'X_preprocessed.csv'), index=False)
    y.to_csv(os.path.join(output_dir, 'y_target.csv'), index=False)
    joblib.dump(scaler, os.path.join(output_dir, 'scaler.pkl'))

    print(f"Preprocessed X, y, and scaler saved to '{output_dir}/'.")
    print("Data preprocessing script finished.")

if __name__ == '__main__':
    main()
