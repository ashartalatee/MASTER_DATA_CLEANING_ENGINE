import pandas as pd
import re

class NumberFormatter:
    def __init__(self, df, rules: dict):
        self.df = df
        self.rules = rules

    def standardize_numbers(self):
        rules = self.rules.get("numeric_standardization", {})

        for column, rule in rules.items():
            if column not in self.df.columns:
                continue

            series = self.df[column].astype(str)

            # Remove currency symbol
            currency = rule.get("currency")
            if currency:
                series = series.str.replace(currency, "", regex=False)

            # Remove percent
            is_percent = rule.get("percent", False)
            if is_percent:
                series = series.str.replace("%", "", regex=False)

            # Handle separators
            thousand_sep = rule.get("thousand_separator")
            decimal_sep = rule.get("decimal_separator")

            if thousand_sep:
                series = series.str.replace(thousand_sep, "", regex=False)

            if decimal_sep and decimal_sep != ".":
                series = series.str.replace(decimal_sep, ".", regex=False)

            # Convert to numeric
            errors = rule.get("errors", "raise")
            series = pd.to_numeric(series, errors=errors)

            # Percent normalization
            if is_percent:
                series = series / 100

            # Cast type
            target_type = rule.get("type")
            if target_type == "int":
                series = series.astype("Int64")
            elif target_type == "float":
                series = series.astype(float)

            self.df[column] = series

        return self.df
