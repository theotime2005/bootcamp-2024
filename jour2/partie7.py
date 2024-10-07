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
    return data

# --------------------------------------------------
def add_columns(orders: pd.DataFrame) -> pd.DataFrame:
    # Ajout de la colonne order_number
    # Utilisation d'un motif répétitif (par exemple 1111, 2222, ...) en fonction de l'index
    orders['order_number'] = ((orders.index + 1) * 1111) % 10000
    
    # Ajout de la colonne unit_price
    # Calcul du prix unitaire comme montant / quantité, arrondi à deux décimales
    orders['unit_price'] = (orders['total_price'] / orders['quantity']).round(2)
    
    return orders

# --------------------------------------------------
def dataframe_operations(data: pd.DataFrame) -> (float, int, float, float, float):
    # Calculer le montant total de toutes les commandes
    total_amount = round(data['amount'].sum(), 2)
    
    # Calculer la quantité totale de produits vendus
    total_quantity = data['quantity'].sum()
    
    # Calculer le prix moyen par commande
    avg_price_per_order = round(total_amount / len(data), 2)
    
    # Trouver le montant maximum de commande
    max_amount = round(data['amount'].max(), 2)
    
    # Trouver le montant minimum de commande
    min_amount = round(data['amount'].min(), 2)
    
    # Retourner un tuple avec les résultats
    return (total_amount, total_quantity, avg_price_per_order, max_amount, min_amount)