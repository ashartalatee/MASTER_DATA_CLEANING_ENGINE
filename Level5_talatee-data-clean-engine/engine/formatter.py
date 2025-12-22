class DataFormatter:
    def __init__(self, df, rules: dict):
        self.df = df
        self.rules = rules

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
                series = series.map(
                    lambda x: mapping.get(x, x)
                )

            self.df[column] = series

        return self.df
