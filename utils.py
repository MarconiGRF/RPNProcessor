import os


class Utils:
    """
    Defines useful methods for the project.
    """
    OPERATORS = ['+', '-', '*', '/']

    @classmethod
    def is_operator(cls, token):
        return token in cls.OPERATORS

    @staticmethod
    def read_expression_from_file():
        expression_tokens = []

        with open(os.path.dirname(__file__) + '/input.stk') as text_file:
            lines = text_file.readlines()
            for (index, line) in enumerate(lines):
                token = line.replace('\n', '')
                expression_tokens.append(token)

        return expression_tokens
