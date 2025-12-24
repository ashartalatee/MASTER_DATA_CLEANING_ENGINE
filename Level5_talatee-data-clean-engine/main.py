import pandas as pd
import yaml

from engine.pipeline import DataCleaningPipeline

def load_rules(path="config/cleaning_rules.yaml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def main():
    df = pd.read_csv("data/raw/sample.csv")
    rules = load_rules()

    pipeline = DataCleaningPipeline(df, rules)
    clean_df = pipeline.run()

    clean_df.to_csv("data/clean/sample_clean.csv", index=False)
    print(" Data cleaning pipeline finished successfully")

if __name__ == "__main__":
    main()