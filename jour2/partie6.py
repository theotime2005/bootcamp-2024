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

# --------------------------------
def pandas_complex_json(file: str, product: dict):
    df = pd.read_json(file)
    df.at[0, 'products'] = product
    df.drop(1, inplace=True)
    df.reset_index(drop=True, inplace=True)
    delete = df.at[2, 'products']
    del delete[1]
    df.at[2, 'products'] = delete
    df.to_json(file, indent=2, orient=  'records')