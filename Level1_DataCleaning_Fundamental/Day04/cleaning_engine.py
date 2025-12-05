import pandas as pd

def clean_data(file_path, output_file="cleaned_output.csv"):
    print("Loading file:", file_path)
    df = pd.read_csv(file_path)

    print("DATA AWAL:", df.shape)

    # 1. Drop duplicates
    df = df.drop_duplicates()

    # 2. standarized text
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].astype(str).str.strip().str.lower()

    # 3. Fix numeric types if exist
    for col in df.columns:
        if "age" in col or "price" in col or "amount" in col:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # 4. Handle missing value
    df = df.fillna("unknown")

    print("CLEANING DONE")
    print("DATA AKHIR:", df.shape)

    # Save result
    df.to_csv(output_file, index=False)
    print("Saved to:", output_file)

    return df