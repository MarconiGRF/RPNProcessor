import os
from rpntoken import RPNToken


class Utils:
    """
    Defines useful methods for the project.
    """
    OPERATORS = ['+', '-', '*', '/']

    @classmethod
    def is_operator(cls, token):
        return token in cls.OPERATORS

    @classmethod
    def is_num(cls, token):
        try:
            int(token)
            return True
        except (TypeError, ValueError):
            return False

    @classmethod
    def classify_token(cls, token):
        if cls.is_num(token):
            return RPNToken("NUM", token)
        elif cls.is_operator(token):
            return RPNToken("OP", token)
        else:
            raise TypeError('Unexpected character: {token}')

    @classmethod
    def read_expression_from_file(cls):
        expression_tokens = []

        with open(os.path.dirname(__file__) + '/input.stk') as text_file:
            lines = text_file.readlines()
            for (index, line) in enumerate(lines):
                token = cls.classify_token(line.replace('\n', ''))
                expression_tokens.append(token)

        return expression_tokens
