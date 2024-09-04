"""
Bootcamp 2024
Jour 1
Partie 6
"""
from typing import Any


def struct_index_display(elems):
    for i in range(len(elems)):
        print(f"{i} = {elems[i]}")


# ------------------------------
def combine_lists(l1: list, l2: list) -> tuple[list[Any] | Any, list[Any] | Any]:
    """
    Combine two lists into a single list
    :param l1: list
    :param l2: list
    :return: None | list
    """
    if len(l1) != len(l2):
        return None
    result = []
    for i in range(len(l1)):
        result.append((l1[i], l2[i]))
    return result


def display_combined_lists(l: list):
    for i in range(len(l)):
        print(f"{i} = {l[i][0]} - {l[i][1]}")


# ------------------------------
def convert_to_string(numbers: list[float]) -> list[str]:
    """
    Convert a list of numbers to a list of strings
    :param numbers: list
    :return: list
    """
    return [str(n) for n in numbers]


def multiply_numbers(l: list[int], multiplicator) -> list[int]:
    """
    Multiply all numbers in a list by a given number
    :param l: list
    :param multiplicator: int
    :return: list
    """
    return [n * multiplicator for n in l]


# ------------------------------
def remove_negatives(numbers: list[float]) -> list[float]:
    """
    Remove all negative numbers from a list
    :param numbers: list
    :return: list
    """
    return [n for n in numbers if n >= 0]


def keep_strings(elements: list) -> list[str]:
    """
    Keep only strings from a list
    :param elements: list
    :return: list
    """
    return [e for e in elements if isinstance(e, str)]


# ------------------------------
def cut_in_two(numbers: list[float]) -> (list[float], list[float]):
    mid = len(numbers) // 2
    return (numbers[:mid], numbers[mid:])
