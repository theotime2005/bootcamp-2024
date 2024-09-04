"""
BootCamp 2024
Jour 2
Partie 3
"""
import sys

import pandas as pd


def create_series() -> pd.Series:
    """
    Create a pdSerie with argv
    :return: pd.Series
    """
    return pd.Series(list(map(int, sys.argv[1:])))


# --------------------
def series_operations(series: pd.Series) -> (int, float, float):
    """
    Perform operations on pd.Series
    :param series: pd.Series
    :return: (sum, mean, std)
    """
    return series.sum(), series.mean(), series.std()


# --------------------
def create_dataframe(products: list[str], quantities: list[int], prices: list[float]) -> pd.DataFrame:
    """
    Create a pd.DataFrame with products, quantities and prices
    :param products: list[str]
    :param quantities: list[int]
    :param prices: list[float]
    :return: pd.DataFrame
    """
    return pd.DataFrame({
        'products': products,
        'quantities': quantities,
        'prices': prices
    })


# --------------------
def dataframe_accession(data: pd.DataFrame) -> tuple:
    """
    Access to data in pd.DataFrame
    :param data: pd.DataFrame
    :return: tuple
    """
    return (data['products'].tolist(), data.iloc[1].to_dict(), data.iloc[3]['quantities'])
