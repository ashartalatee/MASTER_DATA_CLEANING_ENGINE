import os
from cleaning_functions import rename_columns, handle_missing_values, convert_numeric, standardize_date
from file_loader import load_file

input_folder = "data_input"
output_folder = "data_output"
os.makedirs(output_folder, exist_ok=True)

def full_clean_pipeline(df):
    df = rename_columns(df)
    df = handle_missing_values(df)
    df = convert_numeric(df)
    df = standardize_date(df)
    return df

for file_name in os.listdir(input_folder):
    if file_name.startswith(".~lock") or file_name.startswith("."):
        continue  # skip file lock atau hidden
    file_path = os.path.join(input_folder, file_name)
    try:
        df = load_file(file_path)
    except Exception as e:
        print(f"Error loading {file_name}: {e}")
        continue
    
    df_clean = full_clean_pipeline(df)
    
    output_path = os.path.join(output_folder, file_name)
    df_clean.to_csv(output_path, index=False)
    print(f"Processed: {file_name}")
