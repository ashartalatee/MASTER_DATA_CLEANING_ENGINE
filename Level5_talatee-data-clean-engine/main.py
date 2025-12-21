from engine.validator import DataValidator, DataValidationError
import pandas as pd
import yaml

df = pd.read_csv("data/raw/sample.csv")

with open("config/cleaning_rules.yaml") as f:
    rules = yaml.safe_load(f)

validator = DataValidator(df, rules)

try:
    validator.validate_required_columns()
    validator.validate_data_types()
    print(" Validation passed")
except DataValidationError as e:
    print(f" VALIDATION FAILED: {e}")