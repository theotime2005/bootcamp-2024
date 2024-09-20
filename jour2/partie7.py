"""
BootCamp 2024
Jour 2
Partie 7
"""

import pandas as pd

def sort_dataframe_simple(data: pd.DataFrame) -> pd.DataFrame:
    data.sort_values(by = ['product'], ascending=False, inplace=True)
    return data

# --------------------------------------------------
def sort_dataframe_advanced(data: pd.DataFrame) -> pd.DataFrame:
    data.sort_values(by=['quantity'], ascending=True, inplace=True)
    data.sort_values(by=['total_price'], ascending=False, inplace=True)
    data.sort_values(by=['product'], ascending=True, inplace=True)
    data.reset_index(drop=True, inplace=True)
    return data

# --------------------------------------------------
def add_columns(orders: pd.DataFrame) -> pd.DataFrame:
    # Ajout de la colonne order_number
    # Utilisation de l'index, répétition 5 fois, et compression avec modulo 100000 pour garantir 5 chiffres
    orders['order_number'] = (orders.index + 1) % 100000
    
    # Ajout de la colonne unit_price
    # Calcul du prix unitaire comme montant / quantité, arrondi à deux décimales
    orders['unit_price'] = (orders['total_price'] / orders['quantity']).round(2)
    
    return orders

# --------------------------------------------------
