import pandas as pd
import re
from dateutil import parser

# --- Column Cleaner ---
def clean_column_name(col_name):
    col_name = col_name.strip().lower()
    col_name = re.sub(r'\s+', '_', col_name)
    col_name = re.sub(r'[^0-9a-zA-Z_]', '', col_name)
    return col_name

def rename_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    df = df.rename(columns=lambda x: clean_column_name(x))
    return df

# --- Missing Values Handler ---
def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    numeric_cols = df.select_dtypes(include=['number']).columns
    df[numeric_cols] = df[numeric_cols].fillna(0).astype('Int64')  # integer tanpa .0
    string_cols = df.select_dtypes(include=['object']).columns
    df[string_cols] = df[string_cols].fillna("unknown")
    return df

# --- Numeric Cleaner ---
def convert_numeric(df: pd.DataFrame, columns=None) -> pd.DataFrame:
    def to_numeric(val):
        if pd.isna(val):
            return val
        if isinstance(val, str):
            val = re.sub(r'[^\d.-]', '', val)  # hapus simbol Rp, $, koma
            try:
                return float(val)
            except ValueError:
                return pd.NA
        return val
    if columns is None:
        columns = df.select_dtypes(include=['object', 'int', 'float']).columns
    for col in columns:
        df[col] = df[col].apply(to_numeric)
    return df

# --- Date Standardization ---
def standardize_date(df: pd.DataFrame, columns=None, output_format="%Y-%m-%d") -> pd.DataFrame:
    def parse_date(val):
        if pd.isna(val):
            return pd.NA
        try:
            parsed_date = parser.parse(str(val), dayfirst=False, yearfirst=False)
            if parsed_date.year < 100:  # tahun 2 digit → tambah 2000
                parsed_date = parsed_date.replace(year=parsed_date.year + 2000)
            return parsed_date.strftime(output_format)
        except:
            return pd.NA
    if columns is None:
        columns = df.columns
    for col in columns:
        if df[col].dtype == 'object' or 'date' in col.lower():
            df[col] = df[col].apply(parse_date)
    return df
