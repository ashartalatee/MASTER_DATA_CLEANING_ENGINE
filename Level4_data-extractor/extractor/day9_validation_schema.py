import pandas as pd

INPUT_FILE = "output/day8_api_retry.csv"
OUTPUT_FILE = "output/day9_validated_data.csv"

def validate_row(row):
    if not isinstance(row["text"], str) or not row["text"].strip():
        return False
    
    if not isinstance(row["author"], str) or not row["author"].strip():
        return False
    
    if not isinstance(row["tags"], list):
        return False
    
    if row["source"] not in ["web", "api"]:
        return False
    
    return True

df = pd.read_csv(INPUT_FILE)

# Convert tags from string to list if needed
df["tags"] = df["tags"].apply(
    lambda x: eval(x) if isinstance(x, str) and x.startswith("[") else []
)

valid_rows = []
invalid_count = 0

for _, row in df.iterrows():
    if validate_row(row):
        valid_rows.append(row)
    else:
        invalid_count += 1

clean_df = pd.DataFrame(valid_rows)
clean_df.to_csv(OUTPUT_FILE, index=False)

print(f"Valid rows saved: {len(clean_df)}")
print(f"Invalid rows rejected: {invalid_count}")