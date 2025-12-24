class TextFormatter:
    def __init__(self, df, rules):
        self.df = df
        self.rules = rules

    def standardize_text(self):
        rules = self.rules.get("text_standardization", {})

        for column, rule in rules.items():
            if column not in self.df.columns:
                continue

            series = self.df[column].astype(str)

            if rule.get("lowercase"):
                series = series.str.lower()

            if rule.get("strip"):
                series = series.str.strip()

            mapping = rule.get("mapping")
            if mapping:
                series = series.replace(mapping)

            self.df[column] = series

        return self.df
