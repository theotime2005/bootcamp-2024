"""
BootCamp 2024
Jour 2
Partie 4
"""

import pandas as pd


def pandas_csv_read(file: str) -> pd.DataFrame:
    """
    Read a csv file with pandas
    """
    df = pd.read_csv(file)
    return df

# --------------------
def pandas_csv_write(file: str, headers: list, data: list[tuple]):
    """
    Write a csv file using pandas
    :param file: str
    :param headers: list
    :param data: list[tuple]
    """
    # Convert the list of tuples to a DataFrame, excluding the first item of each tuple
    df = pd.DataFrame([d[1:] for d in data], columns=headers)

    # Write the DataFrame to a CSV file
    df.to_csv(file, index=False)