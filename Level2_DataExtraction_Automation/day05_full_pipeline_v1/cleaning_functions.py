import pandas as pd
import re
from dateutil import parser

# --- DAY 1 ---
def clean_column_name(col_name):
    col_name = col_name.strip().lower()
    col_name = re.sub(r'\s+', '_', col_name)
    col_name = re.sub(r'[^0-9a-zA-Z_]', '', col_name)
    return col_name

def rename_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.rename(columns=lambda x: clean_column_name(x))
    return df

# --- DAY 2 ---
def handle_missing_values(df: pd.DataFrame, strategy="fill", fill_value=0) -> pd.DataFrame:
    if strategy == "fill":
        df = df.fillna(fill_value)
    elif strategy == "drop":
        df = df.dropna()
    else:
        raise ValueError("Strategy harus 'fill' atau 'drop'")
    return df

# --- DAY 3 ---
def convert_numeric(df: pd.DataFrame, columns=None) -> pd.DataFrame:
    def to_numeric(val):
        if pd.isna(val):
            return val
        if isinstance(val, str):
            val = re.sub(r'[^\d.-]', '', val)
            try:
                return float(val)
            except ValueError:
                return pd.NA
        return val
    if columns is None:
        columns = df.columns
    for col in columns:
        df[col] = df[col].apply(to_numeric)
    return df

# --- DAY 4 ---
def standardize_date(df: pd.DataFrame, columns=None, output_format="%Y-%m-%d") -> pd.DataFrame:
    def parse_date(val):
        if pd.isna(val):
            return val
        try:
            return parser.parse(str(val)).strftime(output_format)
        except (ValueError, TypeError):
            return pd.NA
    if columns is None:
        columns = df.columns
    for col in columns:
        if df[col].dtype == "object" or "date" in col.lower():
            df[col] = df[col].apply(parse_date)
    return df
