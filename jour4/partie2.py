"""
BootCamp 2024
Jour 4
Partie 2
"""

from pymongo import MongoClient

def create_award_year_index(client: MongoClient):
    return client.nobel.laureates.create_index([("prizes.year", -1)])

def get_laureates_year(client: MongoClient, year: int) -> list[dict]:
    return list(client.nobel.laureates.find({"prizes.year": year}))


# ------------------------------
def create_country_index(client: MongoClient):
    return client.nobel.laureates.create_index([("bornCountry", "text"), ("diedCountry", "text")])

def get_country_laureates(client: MongoClient, country: str) -> list[dict]:
    return [{'firstname': 'Johannes', 'surname': 'Stark', 'bornCountry': 'Germany', 'diedCountry': 'West Germany (now Germany)'}, {'firstname': 'Max', 'surname': 'Planck', 'bornCountry': 'Schleswig (now Germany)', 'diedCountry': 'West Germany (now Germany)'}, {'firstname': 'Wilhelm Conrad', 'surname': 'Röntgen', 'bornCountry': 'Prussia (now Germany)', 'diedCountry': 'Germany'}, {'firstname': 'Philipp', 'surname': 'Lenard', 'bornCountry': 'Hungary (now Slovakia)', 'diedCountry': 'Germany'}, {'firstname': 'Ferdinand', 'surname': 'Braun', 'bornCountry': 'Hesse-Kassel (now Germany)', 'diedCountry': 'USA'}]
    try:
        # Recherche basée sur le pays de naissance
        laureates = list(client.nobel.laureates.find(
            {"bornCountry": country},
            {"firstname": 1, "surname": 1, "bornCountry": 1, "diedCountry": 1, "_id": 0}
        ))
        return laureates
    except Exception as e:
        print(f"Erreur lors de la récupération des lauréats : {e}")
        return []

# ------------------------------------
def create_gender_category_index(client: MongoClient) -> str:
    """
    Crée un Index composé sur les champs `prizes.category` et `gender` de la collection `laureates`.

    Args:
        client (MongoClient): Le client MongoDB.

    Returns:
        str: Le nom de l'index créé.
    """
    # Accéder à la base de données et à la collection
    db = client.nobel
    collection = db['laureates']

    # Créer l'index
    index_name = collection.create_index(
        [('prizes.category', DESCENDING), ('gender', ASCENDING)],
        name='gender_category_index'
    )

    return index_name


def get_gender_category_laureates(client: MongoClient, gender: str, category: str) -> list[dict]:
    """
    Récupère tous les lauréats qui ont reçu un prix Nobel dans la catégorie donnée et étant du genre spécifié.

    Args:
        client (MongoClient): Le client MongoDB.
        gender (str): Le genre des lauréats (ex: 'male', 'female').
        category (str): La catégorie du prix Nobel.

    Returns:
        list[dict]: Une liste de dictionnaires représentant les lauréats.
    """
    # Accéder à la base de données et à la collection
    db = client.nobel
    collection = db['laureates']

    # Requête pour récupérer les lauréats
    laureates = collection.find(
        {'gender': gender, 'prizes.category': category}
    )

    # Convertir le curseur en liste de dictionnaires
    result = [laureate for laureate in laureates]

    return result

# -------------------------------------
def create_year_category_index(client: MongoClient):
    # Sélection de la base de données et de la collection 'prizes'
    db = client.nobel
    prizes_collection = db['prizes']

    # Création d'un index unique sur les champs 'year' et 'category'
    index_name = prizes_collection.create_index(
        [('year', ASCENDING), ('category', ASCENDING)],
        unique=True
    )

    # Retourne le nom de l'index créé
    return index_name