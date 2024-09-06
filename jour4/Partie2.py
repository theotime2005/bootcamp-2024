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
    return list(client.nobel.laureates.find({"$text": {"$search": country}}, {"firstname": 1, "surname": 1, "bornCountry": 1, "diedCountry": 1, "_id": 0}))