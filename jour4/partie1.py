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
    return list(client.nobel.laureates.find({}, {'firstname': 1, 'surname': 1, 'born': 1, '_id': 0}))

def get_prize_categories(client: MongoClient) -> list[str]:
    return list(client.nobel.laureates.distinct("prizes.category"))
print(get_prize_categories(get_mongo_client("localhost", 27017)))

# ------------------------------
def get_category_laureates(client: MongoClient, category: str) -> list[dict]:
    return list(client.nobel.laureates.find({"prizes.category": category}, {"firstname": 1, "surname": 1, "prizes.category": 1, "_id": 0}))


def get_country_laureates(client: MongoClient, country: str) -> list[dict]:
    # Créer une expression régulière pour correspondre à 'country' même s'il apparaît après 'now' ou autre
    regex = re.compile(f".*{re.escape(country)}.*", re.IGNORECASE)

    # Effectuer la requête en utilisant l'expression régulière sur le champ bornCountry
    laureates = client.nobel.laureates.find(
        {"bornCountry": regex},
        {"firstname": 1, "surname": 1, "bornCountry": 1, "_id": 0}
    )

    # Convertir les résultats en liste de dictionnaires
    return list(laureates)

# ------------------------------
def get_shared_prizes(client: MongoClient) -> list[dict]:
    # Pipeline d'aggregation MongoDB
    pipeline = [
        # Décomposer les champs pour chaque lauréat afin d'avoir un document par prix
        {"$unwind": "$prizes"},

        # Groupement par catégorie et année pour compter combien de personnes ont partagé un prix
        {"$group": {
            "_id": {"category": "$prizes.category", "year": "$prizes.year"},
            "count": {"$sum": 1},
            "laureates": {"$push": {"firstname": "$firstname", "surname": "$surname", "share": "$prizes.share"}}
        }},

        # Filtrer les prix qui ont été partagés par plusieurs personnes
        {"$match": {"count": {"$gt": 1}}},

        # Projeter le résultat final
        {"$project": {
            "_id": 0,
            "category": "$_id.category",
            "year": "$_id.year",
            "laureates": 1
        }}
    ]

    # Exécuter le pipeline d'aggregation
    shared_prizes = client.nobel.laureates.aggregate(pipeline)

    # Convertir les résultats en liste de dictionnaires
    return list(shared_prizes)


def get_shared_prizes_common(client: MongoClient) -> list[dict]:
    # Pipeline d'agrégation MongoDB
    pipeline = [
        # Décomposer les prix pour que chaque lauréat et son prix deviennent un document individuel
        {"$unwind": "$prizes"},

        # Groupement par catégorie, année et motivation, et compter combien de personnes ont partagé ce prix
        {"$group": {
            "_id": {"category": "$prizes.category", "year": "$prizes.year", "motivation": "$prizes.motivation"},
            "count": {"$sum": 1},
            "laureates": {"$push": {"firstname": "$firstname", "surname": "$surname", "share": "$prizes.share"}}
        }},

        # Filtrer pour obtenir les prix partagés par exactement 2 personnes
        {"$match": {"count": 2}},

        # Projeter les champs souhaités
        {"$project": {
            "_id": 0,
            "category": "$_id.category",
            "year": "$_id.year",
            "motivation": "$_id.motivation",
            "laureates": 1
        }}
    ]

    # Exécuter le pipeline d'agrégation
    shared_prizes = client.nobel.laureates.aggregate(pipeline)

    # Convertir les résultats en liste de dictionnaires
    return list(shared_prizes)

# ------------------------------
def get_laureates_information_sorted(client: MongoClient) -> list[dict]:
    # Requête pour récupérer les informations des lauréats avec un tri multiple
    laureates = client.nobel.laureates.find(
        {},  # Pas de condition, on récupère tous les lauréats
        {"firstname": 1, "surname": 1, "bornCountry": 1, "born": 1, "_id": 0}
    ).sort([
        ("bornCountry", -1),  # Tri alphabétique inverse par pays de naissance
        ("born", 1)  # Tri croissant par date de naissance
    ])

    # Convertir les résultats en liste de dictionnaires
    return list(laureates)