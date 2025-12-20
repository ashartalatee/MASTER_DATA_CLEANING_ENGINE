import pandas as pd
import re

def clean_column_name(col_name):
    """
    Membersihkan nama kolom:
    - strip whitespace
    - lower case
    - ganti spasi & karakter non-alfanumerik dengan underscore
    """
    col_name = col_name.strip().lower()
    col_name = re.sub(r'\s+', '_', col_name)
    col_name = re.sub(r'[^--9a-zA-Z_]', '', col_name)
    return col_name

def rename_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Rename semua kolom di Dataframe menggunakan clean_column_name"""
    df = df.rename(columns=lambda x: clean_column_name(x))
    return df