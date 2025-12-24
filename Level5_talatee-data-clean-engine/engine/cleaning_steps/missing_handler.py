class MissingValueHandler:
    def __init__(self, df, rules: dict):
        self.df = df
        self.rules = rules

    def handle(self):
        strategies = self.rules.get("missing_value_strategy", {})

        for column, rule in strategies.items():
            if column not in self.df.columns:
                continue

            strategy = rule.get("strategy")

            if strategy == "drop":
                self.df = self.df[self.df[column].notna()]

            elif strategy == "mean":
                self.df[column] = self.df[column].fillna(self.df[column].mean())

            elif strategy == "median":
                self.df[column] = self.df[column].fillna(self.df[column].median())

            elif strategy == "mode":
                self.df[column] = self.df[column].fillna(
                    self.df[column].mode().iloc[0]
                )

            elif strategy == "constant":
                value = rule.get("value")
                self.df[column] = self.df[column].fillna(value)

        return self.df
