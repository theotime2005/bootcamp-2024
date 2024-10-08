"""
BootCamp 2024
Jour 2
Partie 5
"""

import pandas as pd


def pandas_excel_read(file: str, sheet: str) -> pd.DataFrame:
    """
    Read an Excel file and return the content of a specific sheet as a DataFrame
    """
    return pd.read_excel(file, sheet_name=sheet)


# --------------------
def pandas_excel_write(data: pd.DataFrame, filename: str):
    """
    Write a DataFrame to the "orders" sheet in an existing Excel file
    without affecting other sheets.
    """
    try:
        excel_sheets = pd.read_excel(filename, sheet_name=None)
    except FileNotFoundError:
        excel_sheets = {}
    excel_sheets["orders"] = data
    with pd.ExcelWriter(filename, engine='openpyxl') as writer:
        for sheet, sheet_data in excel_sheets.items():
            sheet_data.to_excel(writer, sheet_name=sheet, index=False)


# --------------------
def pandas_excel_selective_read(filename: str) -> pd.DataFrame:
    # Lire le fichier Excel, en sautant les 10 premières lignes et en sélectionnant uniquement les colonnes 'product' et 'total_price'
    df = pd.read_excel(filename, sheet_name='orders', skiprows=10, usecols=['product', 'total_price'])
    
    # Grouper par produit et additionner les montants pour chaque produit
    df_grouped = df.groupby('product', as_index=False).sum()
    
    return df_grouped

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
