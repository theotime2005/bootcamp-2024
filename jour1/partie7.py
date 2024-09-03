"""
BootCamp 2024
Jour 1
Partie 7
"""

def change_separator(base_str: str, split_str: str, join_str: str) -> str:
    cut_str = base_str.split(split_str)
    return join_str.join(cut_str)

# ------------------------------
def  sub_index(base_str: str, sub_str: str) -> str:
    return base_str[base_str.find(sub_str):]

# ------------------------------
def replace_str(base_str: str, sub_str: str) -> str:
    return base_str.replace(sub_str, "Egg and Spam")

# ------------------------------
def  normalize_input(base_str: str) -> (str, str):
    return (base_str.lower(), base_str.upper())

def remove_white_spaces(base_str: str) -> (str, str, str):
    return (base_str.strip(), base_str.lstrip(), base_str.rstrip())