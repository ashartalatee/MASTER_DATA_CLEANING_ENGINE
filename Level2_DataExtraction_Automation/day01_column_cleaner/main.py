import pandas as pd
from cleaning_functions import rename_columns
import os

# folder input & output
input_folder = "data_input"
output_folder = "data_output"
os.makedirs(output_folder, exist_ok=True)

# Loop semua file csv di folder input
for file_name in os.listdir(input_folder):
    if file_name.endswith(".csv"):
        file_path = os.path.join(input_folder, file_name)
        df = pd.read_csv(file_path)

        # rename kolom
        df = rename_columns(df)

        # simpan hasil output
        output_path = os.path.join(output_folder, file_name)
        df.to_csv(output_path, index=False)
        print(f"Processed: {file_name}")