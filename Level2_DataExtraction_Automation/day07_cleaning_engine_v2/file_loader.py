import pandas as pd
import os

def load_file(file_path: str) -> pd.DataFrame:
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".csv":
        return pd.read_csv(file_path)
    elif ext in [".xls", ".xlsx"]:
        return pd.read_excel(file_path)
    elif ext == ".tsv":
        return pd.read_csv(file_path, sep='\t')
    else:
        raise ValueError(f"Format file {ext} tidak didukung")
