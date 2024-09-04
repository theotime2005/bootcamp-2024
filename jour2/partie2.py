"""
BootCamp 2024
Jour 2
Partie 2
"""

import csv


def native_csv_read(file: str) -> list[tuple]:
    """
    Read a csv file and return a list of tuples
    """
    with open(file, mode="r", newline='') as csvfile:
        f = list(csv.reader(csvfile))[1:]
    lst = []
    for i in range(len(f)):
        tmp = [i]+f[i]
        lst.append(tuple(tmp))
    return lst

# ------------------------------
def native_csv_write(file: str, headers: list, data: list[tuple]):
    """
    Write a csv file
    :param file: str
    :param headers: list
    :param data: list 
    """
    with open(file, mode="w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        for d in data:
            writer.writerow(d[1:])