import pandas as pd

class DataValidationError(Exception):
    """Error fatal untuk data yang tidak valid."""
    pass

class DataValidator:
    def __init__(self, df, rules: dict):
        self.df = df
        self.rules = rules

    def validate_required_columns(self):
        required_columns = self.rules.get("required_columns", [])
        missing_columns = [
            col for col in required_columns if col not in self.df.columns
        ]

        if missing_columns:
            raise DataValidationError(
                f"Missing required columns: {missing_columns}"
            )
        
        return True
    
    def validate_data_types(self):
        type_rules = self.rules.get("data_types", {})
        errors = []

        for column, expected_type in type_rules.items():
            if column not in self.df.columns:
                continue # sudahditangani di requered_columns

            series = self.df[column]

            if expected_type == "init":
                if not pd.api.types.is_integer_dtype(series):
                    errors.append(f"{column} should be int")

            elif expected_type == "float":
                if not pd.api.types.is_float_dtype(series):
                        errors.append(f"{column} should be float")

            elif expected_type == "date":
                if not pd.api.types.is_datetime64_any_dtype(series):
                        errors.append(f"{column} should be date")

            elif expected_type == "string":
                if not pd.api.types.is_string_dtype(series):
                        errors.append(f"{column} should be string")

        if errors:
             raise DataValidationError(
                  "Data type validation failed: " + "; ".join(errors)
             )
        return True