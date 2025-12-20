import pandas as pd
import re

# --- DAY 1 FUNCTIONS ---
def clean_column_name(col_name):
    col_name = col_name.strip().lower()
    col_name = re.sub(r'\s+', '_', col_name)
    col_name = re.sub(r'[^0-9a-zA-Z_]', '', col_name)
    return col_name

def rename_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.rename(columns=lambda x: clean_column_name(x))
    return df

# --- DAY 2 FUNCTIONS ---
def handle_missing_values(df: pd.DataFrame, strategy="fill", fill_value=0) -> pd.DataFrame:
    if strategy == "fill":
        df = df.fillna(fill_value)
    elif strategy == "drop":
        df = df.dropna()
    else:
        raise ValueError("Strategy harus 'fill' atau 'drop'")
    return df

# --- DAY 3 FUNCTION ---
def convert_numeric(df: pd.DataFrame, columns=None) -> pd.DataFrame:
    """
    Convert kolom tertentu atau semua kolom numeric ke tipe numeric
    Handle format seperti: '12,000', 'Rp 12.000', '$12.000'
    """
    def to_numeric(val):
        if pd.isna(val):
            return val
        if isinstance(val, str):
            val = re.sub(r'[^\d.-]', '', val)  # hapus simbol & huruf
            try:
                return float(val)
            except ValueError:
                return pd.NA
        return val
    
    if columns is None:
        # coba konversi semua kolom
        columns = df.columns
    
    for col in columns:
        df[col] = df[col].apply(to_numeric)
    
    return df
