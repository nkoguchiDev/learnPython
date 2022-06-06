

def addition(x: int, y: int) -> int:
    return x + y


def subtraction(x: int, y: int) -> int:
    return x - y


def multiplication(x: int, y: int) -> int:
    return x * y


def division(x: int, y: int) -> int:
    if y == 0:
        raise ValueError('Division by zero')
    else:
        return x / y


def sum(li: list) -> int:
    result = 0
    for i in li:
        result += i
    return result
