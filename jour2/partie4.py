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
    Write a csv file with pandas
    """
    df = pd.DataFrame(list(data), columns=headers)
    df.to_csv(file, index=False)