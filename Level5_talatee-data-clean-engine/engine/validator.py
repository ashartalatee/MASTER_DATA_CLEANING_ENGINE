import pandas as pd
from datetime import datetime
class DataValidationError(Exception):
    """Error fatal untuk data yang tidak valid."""
    pass

class DataValidator:
    def __init__(self, df, rules: dict):
        self.df = df
        self.rules = rules

        # Day 5 Required Columns
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
    
    # Day 6 Data Type Validation
    def validate_data_types(self):
        type_rules = self.rules.get("data_types", {})
        errors = []

        for column, expected_type in type_rules.items():
            if column not in self.df.columns:
                continue # sudah ditangani di requered_columns

            series = self.df[column]

            if expected_type == "int":
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
    
    # Day 7 Range & Logic Validation
    def validate_range_and_logic(self):
         range_rules = self.rules.get("range_rules", {})
         errors = []

         for column, rule in range_rules.items():
              if column not in self.df.columns:
                   continue
              
              series = self.df[column]

              if "min" in rule:
                   if (series < rule["min"]).any():
                        errors.append(
                             f"{column} has values below minimum {rule['min']}"
                        )
            
              if "max" in rule:
                   if (series > rule["max"]).any():
                        errors.append(
                             f"{column} has values above maximum {rule['max']}"
                        )

              if rule.get("not_future"):
                   today = pd. Timestamp(datetime.today().date())
                   if (series > today).any():
                        errors.append(
                             f"{column} contains future dates"
                        )

              if errors:
                   raise DataValidationError(
                        "Range & logic validation failed: " + "; ".join(errors)
                   )
              
              return True

#  Day 8
class DataCleaner:
    def __init__(self, df, rules: dict):
        self.df = df
        self.rules = rules

    def handle_missing_values(self):
        strategies = self.rules.get("missing_value_strategy", {})

        for column, rule in strategies.items():
            if column not in self.df.columns:
                continue

            strategy = rule.get("strategy")

            if strategy == "drop":
                self.df = self.df[self.df[column].notna()]

            elif strategy == "mean":
                self.df[column] = self.df[column].fillna(
                    self.df[column].mean()
                )

            elif strategy == "median":
                self.df[column] = self.df[column].fillna(
                    self.df[column].median()
                )

            elif strategy == "mode":
                self.df[column] = self.df[column].fillna(
                    self.df[column].mode().iloc[0]
                )

            elif strategy == "constant":
                value = rule.get("value")
                self.df[column] = self.df[column].fillna(value)

        return self.df

# Day 9 - Duplicate Logic
def handle_duplicates(self):
     duplicate_rules = self.rules.get("duplicate_rules", {})
     subset = duplicate_rules.get("subset")
     keep = duplicate_rules.get("keep", "first")

     if subset:
          self.df = self.df.drop_duplicates(
               subset=subset,
          )

     return self.df