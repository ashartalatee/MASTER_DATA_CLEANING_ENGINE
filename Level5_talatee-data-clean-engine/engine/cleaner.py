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

# Day 10 - Outlier Handling
def handle_outliers(self):
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

          lower_bound = q1 - factor * iqr
          upper_bound = q3 + factor * iqr

          action = rule.get("action", "none")

          if action == "drop":
               self.df = self.df[
                    (self.df[column] >= lower_bound) &
                    (self.df[column] <= upper_bound)
               ]

          elif action == "cap":
               self.df[column] = self.df[column].clip(
                    lower=lower_bound,
                    upper=upper_bound
               )

     return self.df