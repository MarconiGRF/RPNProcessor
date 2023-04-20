import re


class Regex:
    NUM_EXPRESSION = '[0-9]+'
    OP_EXPRESSION = '(\+|-|\*|/)'

    @classmethod
    def is_operator(cls, token):
        match = re.search(cls.OP_EXPRESSION, token)
        if match is not None:
            return True
        else:
            return False

    @classmethod
    def is_num(cls, token):
        match = re.search(cls.NUM_EXPRESSION, token)
        if match is not None:
            return True
        else:
            return False
