import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
import os

# === CONFIGURATION ===
INPUT_PATH = 'C:\ds_intern\IRIS.csv'
OUTPUT_PATH = 'C:\ds_intern\Data.csv'

# === EXTRACT ===
def extract_data(filepath):
    print("Extracting data...")
    return pd.read_csv(filepath)

# === TRANSFORM ===
def transform_data(df):
    print("Transforming data...")

    # Separate features and store original column names
    numeric_features = df.select_dtypes(include=['int64', 'float64']).columns
    categorical_features = df.select_dtypes(include=['object']).columns

    # Pipelines for numeric and categorical data
    numeric_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='mean')),
        ('scaler', StandardScaler())
    ])

    categorical_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('encoder', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
    ])

    # Combine pipelines
    preprocessor = ColumnTransformer([
        ('num', numeric_pipeline, numeric_features),
        ('cat', categorical_pipeline, categorical_features)
    ])

    # Apply transformations
    transformed_array = preprocessor.fit_transform(df)

    # Get transformed column names
    encoded_cat_columns = preprocessor.named_transformers_['cat']['encoder'].get_feature_names_out(categorical_features)
    all_columns = list(numeric_features) + list(encoded_cat_columns)

    # Return transformed DataFrame
    return pd.DataFrame(transformed_array, columns=all_columns)

# === LOAD ===
def load_data(df, filepath):
    print("Loading data...")
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    df.to_csv(filepath, index=False)
    print(f"Processed data saved to {filepath}")

# === RUN PIPELINE ===
def run_pipeline():
    df = extract_data(INPUT_PATH)
    df_transformed = transform_data(df)
    load_data(df_transformed, OUTPUT_PATH)

if __name__ == "__main__":
    run_pipeline()
