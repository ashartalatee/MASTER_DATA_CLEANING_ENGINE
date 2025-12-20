class DataValidatorError(Exception):
    """Error fatal untuk data yang tidak valid."""
    pass

class DataValidator:
    def __init__(self, df, rules: dict):
        self.df = df
        self.rules = rules

    def validate_required_columns(self):
        required_columns = self.rules.get("required_columns", [])
        missing_columns = [
            col for col in required_columns if col not in self.df.columns
        ]

        if missing_columns:
            raise DataValidatorError(
                f"Missing required columns: {missing_columns}"
            )
        
        return True