from collections import deque
from utils import Utils


def check_validity(stack: deque, token: str) -> bool:
    """
    Checks the validity of a token on the given order.

    If the token is an operator while there are only one element on the stack:
     - It is not valid since an operator needs two operands to complete an operation.

    If the token is an operator while there are two elements on the stack:
     - It is valid if there are at least two elements on the stack.
     - It is not valid otherwise.

    If the token is an operand, then it is always valid.

    :param stack: The current stack of operands.
    :param token: The current token to be checked.
    :return: A boolean representing the validity of the token on the current stack state is correct.
    """

    if not Utils.is_operator(token):
        return True
    else:
        if len(stack) < 2:
            return False
        else:
            return True


def handle_validity(stack: deque, token: str):
    """
    Handles token validity using the check_validity rules.

    If the token is not valid for the current state it will raise an error and stop execution.
    :param stack: The current operand stack.
    :param token: The current token being proccessed.
    """
    validity = check_validity(stack, token)

    if validity is not True:
        raise Exception('RPN is not valid, token order is not valid.')
    else:
        pass


def get_operation_result(first_operand: str, second_operand: str, operator: str):
    """
    Gets the result of a mathematic operation with two operands.

    :param first_operand: The first operand of the operation.
    :param second_operand: The second operand of the operation.
    :param operator: The operator of the operation (it can be "+", "-", "*" and "/").
    :return: The numerical result of the operation.
    """
    numeric_first_operand = int(first_operand)
    numeric_second_operand = int(second_operand)

    if operator == '+':
        return numeric_first_operand + numeric_second_operand
    elif operator == '-':
        return numeric_first_operand - numeric_second_operand
    elif operator == '*':
        return numeric_first_operand * numeric_second_operand
    else:
        return numeric_first_operand / numeric_second_operand


def handle_token(stack: deque, token: str):
    """
    Handles the current token for the RPN expression.

    If the token is an operator, then the operation result will be processed and be appended on the stack.
    If the token in an operand, then the operand will only be appended on the stack.
    :param stack:
    :param token:
    :return:
    """
    if Utils.is_operator(token):
        first_operand = stack.pop()
        second_operand = stack.pop()

        operation_result = get_operation_result(first_operand, second_operand, token)
        stack.append(operation_result)
    else:
        stack.append(int(token))


def proccess_rpn():
    """
    Asks for user expresion then processes it and, if the expression is valid, shows the result.
    """
    stack = deque()
    expression_tokens = Utils.read_expression_from_file()

    while len(expression_tokens) != 0:
        token = expression_tokens.pop(0)
        handle_validity(stack, token.lexeme)

        handle_token(stack, token.lexeme)

    final_result = stack.pop()
    print(f'The final result of the RPN expression is: {final_result}')


if __name__ == '__main__':
    proccess_rpn()


