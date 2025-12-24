class DuplicateHandler:
    def __init__(self, df, rules: dict):
        self.df = df
        self.rules = rules

    def handle(self):
        duplicate_rules = self.rules.get("duplicate_rules", {})
        subset = duplicate_rules.get("subset")
        keep = duplicate_rules.get("keep", "first")

        if subset:
            self.df = self.df.drop_duplicates(
                subset=subset,
                keep=keep
            )

        return self.df
