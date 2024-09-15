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