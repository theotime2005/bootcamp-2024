"""
Piscine 2024
Jour 1
Partie 2
"""

def concat_with_space(a: str, b: str) -> str:
    """
    Return strings with space between there
    :param a: str
    :param b: str
    :return: str
    """
    return f"{a} {b}"

# --------------------------------------------
def format_with_fstring(username: str, age: int) -> str:
    """
    Return formatted string with f-string
    :param username: str
    :param age: int
    :return: str
    """
    return f"Hello {username}, you are {age} years old!"
