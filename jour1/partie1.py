"""
Piscine 2024
Jour 1
Partie 1
"""

def multiply(a: int, b: int) -> int:

    """
    Multiply two numbers
    :param a: int
    :param b: int
    :return: int
    """
    return a*b

# ----------------------------
def compare(a: int, b: int):
    """
    Compare a and b and print a sentence
    :param a: int
    :param b: int
    """
    if a>b:
        print("Le premier nombre est plus grand que le second")
    elif a==b:
        print("Les deux nombres sont égaux")
    elif a<b:
        print("Le premier nombre est plus petit que le second")

# ----------------------------
def counting(x):
    """
    Show impaire numbers that 1 to x
    :param x: int
    :return: None
    """
    for n in range(1, x, 2):
        print(f"{n},")
    print(x)

# ----------------------------
def ask_user():
    word = input("Entrer un mot: ")
    while word!="exit":
        print(f"Vous avez entré : {word}")
        return ask_user()

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

def display_square(size: int, char: chr):
    """
    Display a square of size x size with the character char
    """
    for i in range(size):
        print(char*size)