import pandas as pd

# Load CSV
csv_path = "raw/sample.csv"
df_csv = pd.read_csv(csv_path)

print("CSV DATA")
print(df_csv)
print("\nCSV INFO")
print(df_csv.info())

# Load JSON
json_path = "raw/sample.json"
df_json = pd.read_json(json_path)

print("\nJSON DATA")
print(df_json)
print("\nJSON INFO")
print(df_json.info())

# simpan ulang (belum cleaning)
df_csv.to_csv("csv_loaded.csv", index=False)
df_json.to_csv("json_loaded.csv", index=False)

print("\nData berhasil dimuat dan disimpan ulang.")