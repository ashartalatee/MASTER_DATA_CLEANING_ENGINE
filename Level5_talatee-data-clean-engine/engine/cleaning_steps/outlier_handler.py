class OutlierHandler:
    def __init__(self, df, rules: dict):
        self.df = df
        self.rules = rules

    def handle(self):
        outlier_rules = self.rules.get("outlier_rules", {})

        for column, rule in outlier_rules.items():
            if column not in self.df.columns:
                continue

            if rule.get("method") != "iqr":
                continue

            q1 = self.df[column].quantile(0.25)
            q3 = self.df[column].quantile(0.75)
            iqr = q3 - q1
            factor = rule.get("factor", 1.5)

            lower = q1 - factor * iqr
            upper = q3 + factor * iqr

            action = rule.get("action", "none")

            if action == "drop":
                self.df = self.df[
                    (self.df[column] >= lower) &
                    (self.df[column] <= upper)
                ]

            elif action == "cap":
                self.df[column] = self.df[column].clip(lower, upper)

        return self.df
