import pandas as pd

#Load dataset
df = pd.read_csv("dataset_raw.csv")

# Informasi dasar
print("DATA INFO")
print(df.info())

# Sample data
print("SAMPLE DATA")
print(df.head())

# Statistik deskriptif
print("DESKRIPTIVE SUMMARY")
print(df.describe(include='all'))

# Analisis masalah perkolom
# Contoh kategori masalah: missing, duplicate, format, typo, noise
report = []

for col in df.columns:
    missing = df[col].isna().sum()
    duplicates = df[col].duplicated().sum()
    unique = df[col].nunique()
    dtype = df[col].dtype

    issues = []
    if missing > 0:
        issues.append(f"Missing values: {missing}")
    if duplicates > 0:
        issues.append(f"Duplicate values: {duplicates}")
    if dtype == 'object' and unique < 10:
        issues.append(f"Possible typo/category inconsistency")

    report.append({
        "Column": col,
        "Type": dtype,
        "Unique": unique,
        "Issues": "; ".join(issues) if issues else "None"
    })

# Simpan laporan sebagai csv
report_df = pd.DataFrame(report)
report_df.to_csv("day07_issue_report.csv", index=False)
print("\n Laporan masalah dataset tersimpan: 'day07_issue_report.csv'")