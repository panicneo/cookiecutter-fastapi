class APIException(Exception):
    def __init__(self, code: int = 400, message: str = None):
        self.code = code
        self.message = message
