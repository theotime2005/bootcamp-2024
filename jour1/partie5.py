"""
BootCamp 2024
Jour 1
Partie 5
"""
import sys


def list_discovery() -> list:
    """
    :return: list of numbers
    """
    numbers = list(map(int, sys.argv[1:6]))
    numbers = sorted(numbers, reverse=True)
    print(f"Numbers has {len(numbers)} elements and the sum of them all is {sum(numbers)}.")
    numbers.append(int(sys.argv[6]))
    numbers.reverse()

    return numbers


# ------------------------------
def dict_creation() -> dict:
    """
    Use argv to create dict
    :return: dict
    """
    values = sys.argv[1:]
    result = {}
    for i in range(0, len(values) - 1, 2):
        result[values[i]] = values[i + 1]
    return result


def dict_display(my_dict: dict):
    """
    Display the dictionary
    :param my_dict: dict
    """
    list(map(print, my_dict.keys()))
    list(map(print, my_dict.values()))
    for key in my_dict:
        print({key: my_dict[key]})


# ------------------------------
def tuple_discovery(a, b, c, d) -> tuple:
    """
    Return a tuple with d, c, b and a
    :return: tuple
    """
    return (d, c, b, a)


def tuple_display(tpl: tuple):
    """
    Show tuple line by line
    :param tpl: tuple
    """
    for i in tpl:
        print(i)


# ------------------------------
def set_discovery(l1: list, l2: list) -> tuple:
    """
    :param l1: list
    :param l2: list
    :return: tuple
    """
    s1 = set(l1)
    s2 = set(l2)
    set_union = s1.union(s2)
    set_intersection = s1.intersection(s2)
    set_difference = s1.difference(s2)
    set_symetric_difference = s1.symmetric_difference(s2)
    return (set_union, set_intersection, set_difference, set_symetric_difference)


# ------------------------------
def power_via_comprehension(numbers: list[int]) -> list[int]:
    """
    :param numbers: list
    :return: list
    """
    new_list = []
    for number in numbers:
        if number > 0:
            new_list.append(number * -1)
        elif number < 0:
            new_list.append(number ** 2)
    return new_list


print(power_via_comprehension([1, 2, 3, -4, -5, 6, -7, 8, 9, -10]))
