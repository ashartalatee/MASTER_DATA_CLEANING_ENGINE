import pandas as pd
import re

# Day 1 functions
def clean_column_name(col_name):
    col_name = col_name.strip().lower()
    col_name = re.sub(r'\s+', '_', col_name)
    col_name = re.sub(r'[^0-9a-zA-Z_]', '', col_name)
    return col_name

def rename_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.rename(columns=lambda x: clean_column_name(x))
    return df

# Day 2 function
def handle_missing_values(df: pd.DataFrame, strategy="fill", fill_value=0) -> pd.DataFrame:
    """
    Menghandle missing values (NaN) di DataFrame
    strategy: 
      - 'fill' → isi NaN dengan fill_value
      - 'drop' → hapus baris yang ada NaN
    """
    if strategy == "fill":
        df = df.fillna(fill_value)
    elif strategy == "drop":
        df = df.dropna()
    else:
        raise ValueError("Strategy harus 'fill' atau 'drop'")
    return df