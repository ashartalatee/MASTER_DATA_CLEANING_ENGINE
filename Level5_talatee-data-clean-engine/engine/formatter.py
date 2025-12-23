import pandas as pd


class DataFormatter:
    def __init__(self, df, rules: dict):
        self.df = df
        self.rules = rules

    # DAY 11 — TEXT STANDARDIZATION
    def standardize_text(self):
        rules = self.rules.get("text_standardization", {})

        for column, rule in rules.items():
            if column not in self.df.columns:
                continue

            series = self.df[column].astype(str)

            if rule.get("strip"):
                series = series.str.strip()

            if rule.get("lowercase"):
                series = series.str.lower()

            if rule.get("uppercase"):
                series = series.str.upper()

            mapping = rule.get("mapping")
            if mapping:
                series = series.map(lambda x: mapping.get(x, x))

            self.df[column] = series

        return self.df

    # DAY 12 — DATE STANDARDIZATION
    def standardize_dates(self):
        rules = self.rules.get("date_standardization", {})

        for column, rule in rules.items():
            if column not in self.df.columns:
                continue

            errors = rule.get("errors", "raise")

            # Parsing ke datetime
            self.df[column] = pd.to_datetime(
                self.df[column],
                errors=errors
            )

            # Formatting output (opsional)
            date_format = rule.get("format")
            if date_format:
                self.df[column] = self.df[column].dt.strftime(date_format)

        return self.df
