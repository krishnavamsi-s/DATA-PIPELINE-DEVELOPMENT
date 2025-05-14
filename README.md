# DATA-PIPELINE-DEVELOPMENT
# IRIS Dataset ETL Pipeline

This project contains a simple ETL (Extract-Transform-Load) pipeline implemented in Python using `pandas` and `scikit-learn`. It processes the IRIS dataset by cleaning, transforming, and saving the data for further analysis or modeling.

## 📌 What It Does

- **Extracts** raw data from a CSV file.
- **Transforms**:
  - Imputes missing values (mean for numeric, most frequent for categorical).
  - Scales numeric features using `StandardScaler`.
  - Encodes categorical features with `OneHotEncoder`.
- **Loads** the cleaned data into a new CSV file.

## 🧾 File Included

- `data_pipeline.py`: Main Python script containing the ETL logic.

## 📂 File Paths

Make sure to set correct file paths in the script:

```python
INPUT_PATH = 'C:\\ds_intern\\IRIS.csv'
OUTPUT_PATH = 'C:\\ds_intern\\Data.csv'
