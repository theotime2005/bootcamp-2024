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
    first_products = df.at[0, 'products']
    first_products.append(new_product)
    df.at[0, 'products'] = first_products  # Réassigner la liste modifiée

    # Étape 2 : Supprimer la deuxième transaction
    if len(df) > 1:
        df = df.drop(1).reset_index(drop=True)  # Réindexer après suppression

    # Étape 3 : Supprimer le deuxième produit de la troisième transaction (si existe)
    if len(df) > 2 and len(df.at[2, 'products']) > 1:
        third_products = df.at[2, 'products']
        del third_products[1]
        df.at[2, 'products'] = third_products  # Réassigner la liste modifiée

    # Sauvegarder les modifications dans le fichier JSON avec une indentation de 2 espaces
    # Convertir en liste de dictionnaires
    data_dict = df.to_dict(orient='records')
    with open(filename, 'w') as f:
        json.dump(data_dict, f, indent=2)