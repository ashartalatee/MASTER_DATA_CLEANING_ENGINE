from engine.cleaning_steps.missing_handler import MissingValueHandler
from engine.cleaning_steps.duplicate_handler import DuplicateHandler
from engine.cleaning_steps.outlier_handler import OutlierHandler

from engine.formatter.text_formatter import TextFormatter
from engine.formatter.date_formatter import DateFormatter
from engine.formatter.number_formatter import NumberFormatter

class DataCleaner:
    def __init__(self, df, rules):
        self.df = df
        self.rules = rules

    def clean(self):
        steps = self.rules.get("cleaning_steps", {})

        if steps.get("missing"):
            self.df = MissingValueHandler(self.df, self.rules).handle()

        if steps.get("duplicate"):
            self.df = DuplicateHandler(self.df, self.rules).handle()

        if steps.get("outlier"):
            self.df = OutlierHandler(self.df, self.rules).handle()

        # Formatter layer
        self.df = TextFormatter(self.df, self.rules).standardize_text()
        self.df = DateFormatter(self.df, self.rules).standardize_dates()
        self.df = NumberFormatter(self.df, self.rules).standardize_numbers()

        return self.df
