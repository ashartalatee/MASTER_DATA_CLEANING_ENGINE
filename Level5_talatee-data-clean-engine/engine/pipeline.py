from engine.validator import DataValidator
from engine.cleaner import DataCleaner

class DataCleaningPipeline:
    def __init__(self, df, rules):
        self.df = df
        self.rules = rules

    def run(self):
        validator = DataValidator(self.df, self.rules)
        validator.validate_required_columns()
        validator.validate_data_types()

        cleaner = DataCleaner(self.df, self.rules)
        cleaned_df = cleaner.clean()

        return cleaned_df
