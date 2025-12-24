from engine.cleaning_steps.missing_handler import MissingValueHandler
from engine.cleaning_steps.duplicate_handler import DuplicateHandler
from engine.cleaning_steps.outlier_handler import OutlierHandler

class DataCleaner:
    def __init__(self, df, rules: dict):
        self.df = df
        self.rules = rules

    def clean(self):
        self.df = MissingValueHandler(self.df, self.rules).handle()
        self.df = DuplicateHandler(self.df, self.rules).handle()
        self.df = OutlierHandler(self.df, self.rules).handle()
        return self.df
