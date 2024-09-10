"""
BootCamp 2024
Jour 6
Partie 2
"""

import pandas as pd

def  	create_multi_index_df(df: pd.DataFrame) -> pd.DataFrame :
    """
    Crée un DataFrame avec un index multi-niveaux
    """
    df = df.set_index(['year', 'region'])
    return df

# ------------------------------------
def retrieve_multi_index_data(df: pd.DataFrame, year: int, region: str) -> pd.DataFrame:
    return df.loc[(year, region)]

# ------------------------------------
def multi_index_aggregate(df: pd.DataFrame) -> pd.DataFrame:
    aggregated_df = df.groupby(['year', 'region']).agg({
        'produit_vendu': 'sum',
        'ventes': 'sum'
    })
    aggregated_df = aggregated_df.round(2)

    return aggregated_df

# ------------------------------------
def columns_multi_index(df: pd.DataFrame) -> pd.DataFrame:
    # Groupement par 'year', 'region' et 'categorie' et agrégation des données
    aggregated_df = df.groupby(['year', 'region', 'categorie']).agg({
        'produit_vendu': 'sum',
        'ventes': 'sum'
    })

    # On arrondit les résultats à deux décimales
    aggregated_df = aggregated_df.round(2)

    # Pivot de la table pour que 'categorie' devienne un multi-index pour les colonnes
    pivot_df = aggregated_df.unstack(level='categorie')

    # Retourner le DataFrame avec colonnes multi-indexées
    return pivot_df


def swap_columns_multi_index(df: pd.DataFrame) -> pd.DataFrame:
    # Inverser les niveaux du multi-index des colonnes
    swapped_df = df.swaplevel(axis=1)

    # Trier les colonnes pour que l'ordre soit correct (catégorie, puis 'produit_vendu' et 'ventes')
    swapped_df = swapped_df.sort_index(axis=1)

    # Retourner le DataFrame modifié
    return swapped_df

# ------------------------------------
def retrieve_multi_index_column(df: pd.DataFrame, category: str) -> pd.DataFrame:
    # Sélectionner uniquement les colonnes pour la catégorie donnée
    return df[category]


def retrieve_multi_index_basic(df: pd.DataFrame, category: str, year: int) -> pd.DataFrame:
    # Filtrer d'abord par l'année donnée dans l'index (niveau 'year')
    filtered_df = df.loc[year]

    # Sélectionner uniquement les colonnes pour la catégorie donnée
    return filtered_df[category]


def retrieve_multi_index_advanced(df: pd.DataFrame, region: str, sub_column: str) -> pd.DataFrame:
    # Sélectionner toutes les lignes pour la région donnée
    filtered_df = df.xs(region, level='region')

    # Sélectionner uniquement les colonnes pour le sous-niveau spécifié (quantity ou total_price)
    return filtered_df.xs(sub_column, level=1, axis=1)
