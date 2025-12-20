from engine.validator import DataValidator, DataValidatorError
import pandas as pd
import yaml

df = pd.read_csv("data/raw/sample.csv")

with open("config/cleaning_rules.yaml") as f:
    rules = yaml.safe_load(f)

validator = DataValidator(df, rules)

try:
    validator.validate_required_columns()
    print(" Required columns OK")
except DataValidatorError as e:
    print(f" VALIDATION FAILED: {e}")