def multiply(a: int, b: int) -> int:

    """
    Multiply two numbers
    :param a: int
    :param b: int
    :return: int
    """
    return a*b

# ----------------------------
def safe_divide(a: int, b: int) -> float | None:
    """
    Divide a by b and return the result
    :param a: int
    :param b: int
    :return: float | None
    """
    try:
        return a / b
    except:
        return None