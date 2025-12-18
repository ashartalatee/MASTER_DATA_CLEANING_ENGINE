import os
import csv

# Import hasil Day 3
# Pastikan day3_pagination.py berada di folder yang sama
from day3_pagination import all_results  

# 1. Buang duplicate berdasarkan 'text'
seen = set()
cleaned = []
for item in all_results:
    if item['text'] not in seen:
        seen.add(item['text'])
        cleaned.append(item)

# 2. Standarisasi text & tags
for item in cleaned:
    item['text'] = item['text'].strip()
    item['author'] = item['author'].strip()
    item['tags'] = [t.strip().lower() for t in item['tags']]

# 3. Cek missing data (text & author wajib ada)
final_data = [item for item in cleaned if item['text'] and item['author']]

# 4. Siapkan folder output & path CSV
script_dir = os.path.dirname(os.path.abspath(__file__))   # folder script
output_folder = os.path.join(script_dir, "../output")      # naik 1 level → output
os.makedirs(output_folder, exist_ok=True)
output_file = os.path.join(output_folder, "quotes_cleaned.csv")

# 5. Simpan ke CSV
with open(output_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['text', 'author', 'tags'])
    writer.writeheader()
    for row in final_data:
        row_copy = row.copy()
        row_copy['tags'] = ','.join(row_copy['tags'])  # gabungkan list tags jadi string
        writer.writerow(row_copy)

print(f"Cleaned data saved: {len(final_data)} rows")
print(f"CSV path: {output_file}")
