"""
BootCamp 2024
Jour 2
Partie 6
"""
import json
import pandas as pd


def pandas_json_read(file: str) -> pd.DataFrame:
    """
    This function reads a json file and return a dataframe
    :param file: str
    :return: pd.DataFrame
    """
    return pd.read_json(file)


# --------------------------------
def pandas_json_write(file: str, data: pd.DataFrame):
    """
    This function writes a dataframe to a json file
    :param file: str
    :param data: pd.DataFrame
    """
    data.to_json(file, indent=4, orient="records")