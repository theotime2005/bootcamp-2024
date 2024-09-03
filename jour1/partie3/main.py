import operations as operations

def do_op(a: int, b: int, op: chr) -> float | int | None:
    """
    :param a: int
    :param b: int
    :param op: chr
    :return: float | int | None
    """
    if op=="+":
        return operations.add(a,b)
    elif op=="-":
        return operations.subtract(a,b)
    elif op=="*":
        return operations.multiply(a,b)
    elif op=="/":
        return operations.safe_divide(a,b)
    return None
print(do_op(2,6,"*"))
print(do_op(3,4,"+"))
print(do_op(10,2,"/"))
print(do_op(10,2,"-"))