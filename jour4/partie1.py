"""
BootCamp 2024
Jour 4
Partie 1
"""

from pymongo import MongoClient

def get_mongo_client(host: str, port: int) -> MongoClient:
    return MongoClient(host, port)

# ------------------------------
def get_all_laureates(client: MongoClient) -> list[dict]:
    return list(client.nobel.laureates.find())

# ------------------------------
def get_laureates_information(client: MongoClient) -> list[dict]:
    return list(client.nobel.laureates.find({"prizes.category": "physics"}, {"firstname": 1, "surname": 1, "prizes.category": 1, "_id": 0}))

def get_country_laureates(client: MongoClient, country: str) -> list[dict]:
    return list(client.nobel.laureates.find({"bornCountry": country}, {"firstname": 1, "surname": 1, "bornCountry": 1, "_id": 0}))

# ------------------------------
def get_shared_prizes(client: MongoClient) -> list[dict]:
    return list(client.nobel.laureates.find({"prizes.share": {"$gt": 1}}, {"firstname": 1, "surname": 1, "prizes.share": 1, "_id": 0}))

def get_shared_prizes_common(client: MongoClient) -> list[dict]:
    return list(client.nobel.laureates.find({"prizes.share": 1}, {"firstname": 1, "surname": 1, "prizes.share": 1, "_id": 0}))