class RPNToken:
    type = None
    lexeme = None

    def __init__(self, token_type, lexeme):
        self.type = token_type
        self.lexeme = lexeme
