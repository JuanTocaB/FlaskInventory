
class ProductError(Exception):
    def __init__(self, message: str, error_code: int):
        super().__init__(message)
        self.message = message
        self.error_code = error_code

    def __str__(self) ->str:
        return f"{self.message} (Error Code: {self.error_code})"
