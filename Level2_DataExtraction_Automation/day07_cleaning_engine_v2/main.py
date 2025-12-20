import os
import json
from datetime import datetime
import logging
from cleaning_functions import rename_columns, handle_missing_values, convert_numeric, standardize_date
from file_loader import load_file

# Load config
with open("config.json", "r") as f:
    config = json.load(f)

# Setup folders
input_folder = "data_input"
output_folder = "data_output"
log_folder = "logs"
os.makedirs(output_folder, exist_ok=True)
os.makedirs(log_folder, exist_ok=True)

# Setup logging
logging.basicConfig(
    filename=config["log_file"],
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def full_clean_pipeline(df):
    df = rename_columns(df)
    df = handle_missing_values(df, fill_string=config["fill_string"], fill_numeric=config["fill_numeric"])
    df = convert_numeric(df)
    df = standardize_date(df, date_format=config["date_format"])
    return df

# Process files
for file_name in os.listdir(input_folder):
    file_path = os.path.join(input_folder, file_name)
    ext = os.path.splitext(file_name)[1].lower()
    
    if ext not in config["supported_extensions"]:
        logging.warning(f"Skipped unsupported file: {file_name}")
        continue
    
    try:
        df = load_file(file_path)
        logging.info(f"Loaded file: {file_name}")
    except Exception as e:
        logging.error(f"Error loading {file_name}: {e}")
        continue
    
    df_clean = full_clean_pipeline(df)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"{config['output_prefix']}{timestamp}_{file_name}"
    output_path = os.path.join(output_folder, output_file)
    
    df_clean.to_csv(output_path, index=False)
    logging.info(f"Processed and saved: {output_file}")
    print(f"Processed: {output_file}")
