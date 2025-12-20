import pandas as pd
from cleaning_functions import rename_columns, handle_missing_values
import os

input_folder = "data_input"
output_folder = "data_output"
os.makedirs(output_folder, exist_ok=True)

for file_name in os.listdir(input_folder):
    if file_name.endswith(".csv"):
        file_path = os.path.join(input_folder, file_name)
        df = pd.read_csv(file_path)
        
        # 1. Rename kolom
        df = rename_columns(df)
        
        # 2. Handle missing values
        df = handle_missing_values(df, strategy="fill", fill_value=0)
        
        # Simpan hasil
        output_path = os.path.join(output_folder, file_name)
        df.to_csv(output_path, index=False)
        print(f"Processed: {file_name}")
