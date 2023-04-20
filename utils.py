import os

from regex import Regex
from rpntoken import RPNToken


class Utils:
    """
    Defines useful methods for the project.
    """

    @classmethod
    def classify_token(cls, token):
        if Regex.is_num(token):
            return RPNToken("NUM", token)
        elif Regex.is_operator(token):
            return RPNToken("OP", token)
        else:
            raise TypeError('Unexpected character: {token}')

    @classmethod
    def scan_file(cls):
        expression_tokens = []

        with open(os.path.dirname(__file__) + '/input.stk') as text_file:
            lines = text_file.readlines()
            for (index, line) in enumerate(lines):
                token = cls.classify_token(line.replace('\n', ''))
                expression_tokens.append(token)

        return expression_tokens
