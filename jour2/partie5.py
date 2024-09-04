"""
BootCamp 2024
Jour 2
Partie 5
"""
from functools import total_ordering

import pandas as pd

def pandas_excel_read(file: str, sheet: str) -> pd.DataFrame:
    """
    Read an Excel file and return the content of a specific sheet as a DataFrame
    """
    return pd.read_excel(file, sheet_name=sheet)

# --------------------
def pandas_excel_write(data: pd.DataFrame, filename: str):
    """
    Write a DataFrame to an Excel file
    """
    data.to_excel(filename, sheet_name="orders", index=False)

# --------------------
def pandas_excel_selective_read(filename: str) -> pd.DataFrame :
    """
    Read an Excel file and return the content of a specific sheet as a DataFrame
    :param filename: str
    :return: pd.DataFrame
    """
    data = pd.read_excel(filename, sheet_name="orders").iloc[11:][['product', 'total_price']]
    return data.drop_duplicates(subset=['product'])

# --------------------
def pandas_excel_manipulation(filename: str):
    """
    Read an Excel file and return the content of a specific sheet as a DataFrame
    :param filename: str
    :return: pd.DataFrame
    """
    data = pd.read_excel(filename, sheet_name="orders")
    summary = data.groupby(['product']).agg(
        total_orders=('product', 'size'),
        total_quantity=('quantity', 'sum')
    )
    summary['mean_quantity_per_order'] = (summary['total_quantity'] / summary['total_orders']).round(2)
    summary.reset_index(inplace=True)
    with pd.ExcelWriter(filename, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        summary.to_excel(writer, sheet_name='summary', index=False)
