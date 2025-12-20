import pandas as pd

raw = pd.read_csv("../data/raw/dataset_raw.csv")
clean = pd.read_csv("../data/processed/dataset_step3_standardized.csv")

report = []

report.append("# Data Cleaning Report (Day 19)\n")
report.append("## 1. Dataset Summary (Before Cleaning)")
report.append(f"- Total Rows: {raw.shape[0]}")
report.append(f"- Total Columns: {raw.shape[1]}")

report.append("\n## 2. Issues Found")
report.append("- Duplicate rows")
report.append("- Missing values (name, age)")
report.append("- Typos in email (gmailcom, @@)")
report.append("- Inconsistent phone number format")
report.append("- Multiple date formats")

report.append("\n## 3. Cleaning Steps Applied")
report.append("1. Removed duplicates")
report.append("2. Filled missing age with median")
report.append("3. Replaced empty names with 'Unknown'")
report.append("4. Standardized email typo")
report.append("5. Cleaned phone number (digits only)")
report.append("6. Standardized join_date to datetime format")

report.append("\n## 4. Dataset Summary (After Cleaning)")
report.append(f"- Total Rows: {clean.shape[0]}")
report.append(f"- Total Columns: {clean.shape[1]}")

report.append("\n## 5. Notes")
report.append("- Script dipecah menjadi beberapa step agar mudah dipahami")
report.append("- Struktur folder dibuat seperti proyek profesional")
report.append("- Laporan ini bisa dipakai untuk komunikasi dengan client / atasan")

with open("../report/cleaning_report.md", "w") as f:
    f.write("\n".join(report))

print("Step 4 done: cleaning report generated")
