"""
BootCamp 2024
Jour 2
Partie 6
"""

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
def pandas_complex_json(filename: str, new_product: dict):
    """
    Modifie un fichier JSON en utilisant Pandas :
    1. Ajoute un nouveau produit à la première transaction.
    2. Supprime la deuxième transaction.
    3. Supprime le deuxième produit de la troisième transaction.

    :param filename: str - Nom du fichier JSON.
    :param new_product: dict - Dictionnaire contenant les informations du nouveau produit.
    """
    # Charger le fichier JSON dans un DataFrame
    df = pd.read_json(filename)

    # Étape 1 : Ajouter un nouveau produit à la première transaction
    df.at[0, 'products'].append(new_product)

    # Étape 2 : Supprimer la deuxième transaction
    if len(df) > 1:
        df = df.drop(1)

    # Étape 3 : Supprimer le deuxième produit de la troisième transaction (si existe)
    if len(df) > 2 and len(df.at[2, 'products']) > 1:
        del df.at[2, 'products'][1]

    # Sauvegarder les modifications dans le même fichier JSON avec une indentation de 2 espaces
    df.to_json(filename, orient='records', indent=2)