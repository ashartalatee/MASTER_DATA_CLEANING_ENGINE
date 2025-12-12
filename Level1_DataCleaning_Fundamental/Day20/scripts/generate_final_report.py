import pandas as pd

raw = pd.read_csv("../data/raw/client_dataset_raw.csv")
clean = pd.read_csv("../data/processed/client_dataset_clean.csv")

report = []

report.append("# Client Data Cleaning Report (Day 20)\n")

report.append("## 1. Initial Dataset Summary")
report.append(f"- Rows: {raw.shape[0]}")
report.append(f"- Columns: {raw.shape[1]}\n")

report.append("## 2. Issues Identified")
report.append("- Duplicate rows")
report.append("- Missing names")
report.append("- Missing purchase_total")
report.append("- Invalid email formats")
report.append("- Inconsistent phone formats")
report.append("- Mixed date formats\n")

report.append("## 3. Cleaning Steps Applied")
report.append("1. Removed duplicates")
report.append("2. Fixed missing values (name, purchase_total)")
report.append("3. Standardized email formats")
report.append("4. Normalized phone numbers")
report.append("5. Converted signup_date to datetime format\n")

report.append("## 4. Final Dataset Summary")
report.append(f"- Rows: {clean.shape[0]}")
report.append(f"- Columns: {clean.shape[1]}\n")

report.append("## 5. Notes & Recommendations")
report.append("- Disarankan client memperbaiki format input di sistem mereka")
report.append("- Email validation harus ditambahkan di sistem real")
report.append("- Hasil final siap dipakai untuk analisis lanjutan\n")

with open("../report/client_cleaning_report.md", "w") as f:
    f.write("\n".join(report))

print("Final Report Generated!")
