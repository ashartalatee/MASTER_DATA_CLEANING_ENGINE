import os
from ..engine.cleaning_engine import clean_data

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

INPUT_FOLDER = os.path.join(BASE_DIR, "input_data")
OUTPUT_FOLDER = os.path.join(BASE_DIR, "output_data")

for file in os.listdir(INPUT_FOLDER):
    if file.endswith(".csv"):
        input_path = os.path.join(INPUT_FOLDER, file)
        output_path = os.path.join(OUTPUT_FOLDER, f"cleaned_{file}")

        clean_data(input_path, output_path)
        print(f"✅ Cleaned: {file}")
