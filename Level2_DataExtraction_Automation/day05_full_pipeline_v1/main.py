import pandas as pd
from cleaning_functions import rename_columns, handle_missing_values, convert_numeric, standardize_date
import os

input_folder = "data_input"
output_folder = "data_output"
os.makedirs(output_folder, exist_ok=True)

def full_clean_pipeline(df: pd.DataFrame) -> pd.DataFrame:
    """Pipeline end-to-end: Column rename → NaN → Numeric → Date"""
    df = rename_columns(df)
    df = handle_missing_values(df, strategy="fill", fill_value=0)
    df = convert_numeric(df)
    df = standardize_date(df)
    return df

for file_name in os.listdir(input_folder):
    if file_name.endswith(".csv"):
        file_path = os.path.join(input_folder, file_name)
        df = pd.read_csv(file_path)
        
        # Jalankan full pipeline
        df_clean = full_clean_pipeline(df)
        
        # Simpan hasil
        output_path = os.path.join(output_folder, file_name)
        df_clean.to_csv(output_path, index=False)
        print(f"Processed: {file_name}")
