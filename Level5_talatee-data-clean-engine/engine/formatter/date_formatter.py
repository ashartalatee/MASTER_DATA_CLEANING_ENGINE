import pandas as pd

class DateFormatter:
    def __init__(self, df, rules: dict):
        self.df = df
        self.rules = rules

    def standardize_dates(self):
        rules = self.rules.get("date_standardization", {})

        for column, rule in rules.items():
            if column not in self.df.columns:
                continue

            errors = rule.get("errors", "raise")

            self.df[column] = pd.to_datetime(
                self.df[column],
                errors=errors
            )

            date_format = rule.get("format")
            if date_format:
                self.df[column] = self.df[column].dt.strftime(date_format)

        return self.df
