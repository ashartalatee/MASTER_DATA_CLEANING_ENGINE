import pandas as pd
import re

def clean_data(input_path, output_path):

    df = pd.read_csv(input_path)

    # Bersihkan kolom teks
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].astype(str)

        # hapus simbol aneh
        df[col] = df[col].apply(lambda x: re.sub(r"[^a-zA-Z0-9 ,.-]", "", x))

        # hapus spasi berlebihan
        df[col] = df[col].apply(lambda x: x.strip())

    # simpan hasil
    df.to_csv(output_path, index=False)

    print(f"✅ Saved cleaned file to: {output_path}")
