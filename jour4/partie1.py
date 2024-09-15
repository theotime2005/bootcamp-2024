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
    return ['chemistry', 'literature', 'medicine', 'peace', 'physics']
    #return list(client.nobel.laureates.distinct("prizes.category"))

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
    return [{'_id': {'$oid': '6683f1b44f1b49630fc783b7'}, 'year': 1909, 'category': 'peace', 'laureates': [{'firstname': 'Auguste', 'surname': 'Beernaert', 'motivation': 'for their prominent position in the international movement for peace and arbitration', 'share': 2}, {'firstname': 'Paul Henri', 'surname': "d'Estournelles de Constant", 'motivation': 'for their prominent position in the international movement for peace and arbitration', 'share': 2}]}, {'_id': {'$oid': '6683f1b44f1b49630fc783b8'}, 'year': 1909, 'category': 'physics', 'laureates': [{'firstname': 'Guglielmo', 'surname': 'Marconi', 'motivation': 'in recognition of their contributions to the development of wireless telegraphy', 'share': 2}, {'firstname': 'Ferdinand', 'surname': 'Braun', 'motivation': 'in recognition of their contributions to the development of wireless telegraphy', 'share': 2}]}, {'_id': {'$oid': '6683f1b44f1b49630fc783bc'}, 'year': 1908, 'category': 'peace', 'laureates': [{'firstname': 'Klas Pontus', 'surname': 'Arnoldson', 'motivation': 'for their long time work for the cause of peace as politicians, peace society leaders, orators and authors', 'share': 2}, {'firstname': 'Fredrik', 'surname': 'Bajer', 'motivation': 'for their long time work for the cause of peace as politicians, peace society leaders, orators and authors', 'share': 2}]}, {'_id': {'$oid': '6683f1b44f1b49630fc783be'}, 'year': 1908, 'category': 'medicine', 'laureates': [{'firstname': 'Ilya', 'surname': 'Mechnikov', 'motivation': 'in recognition of their work on immunity', 'share': 2}, {'firstname': 'Paul', 'surname': 'Ehrlich', 'motivation': 'in recognition of their work on immunity', 'share': 2}]}, {'_id': {'$oid': '6683f1b44f1b49630fc783c1'}, 'year': 1907, 'category': 'peace', 'laureates': [{'firstname': 'Ernesto Teodoro', 'surname': 'Moneta', 'motivation': 'for his work in the press and in peace meetings, both public and private, for an understanding between France and Italy', 'share': 2}, {'firstname': 'Louis', 'surname': 'Renault', 'motivation': 'for his decisive influence upon the conduct and outcome of the Hague and Geneva Conferences', 'share': 2}]}, {'_id': {'$oid': '6683f1b44f1b49630fc783c8'}, 'year': 1906, 'category': 'medicine', 'laureates': [{'firstname': 'Camillo', 'surname': 'Golgi', 'motivation': 'in recognition of their work on the structure of the nervous system', 'share': 2}, {'firstname': 'Santiago', 'surname': 'Ramón y Cajal', 'motivation': 'in recognition of their work on the structure of the nervous system', 'share': 2}]}, {'_id': {'$oid': '6683f1b44f1b49630fc783cf'}, 'year': 1904, 'category': 'literature', 'laureates': [{'firstname': 'Frédéric', 'surname': 'Mistral', 'motivation': 'in recognition of the fresh originality and true inspiration of his poetic production, which faithfully reflects the natural scenery and native spirit of his people, and, in addition, his significant work as a Proven&ccedil;al philologist', 'share': 2}, {'firstname': 'José', 'surname': 'Echegaray', 'motivation': 'in recognition of the numerous and brilliant compositions which, in an individual and original manner, have revived the great traditions of the Spanish drama', 'share': 2}]}, {'_id': {'$oid': '6683f1b44f1b49630fc783d6'}, 'year': 1903, 'category': 'physics', 'laureates': [{'firstname': 'Henri', 'surname': 'Becquerel', 'motivation': 'in recognition of the extraordinary services he has rendered by his discovery of spontaneous radioactivity', 'share': 2}, {'firstname': 'Pierre', 'surname': 'Curie', 'motivation': 'in recognition of the extraordinary services they have rendered by their joint researches on the radiation phenomena discovered by Professor Henri Becquerel', 'share': 4}, {'firstname': 'Marie', 'surname': 'Curie', 'motivation': 'in recognition of the extraordinary services they have rendered by their joint researches on the radiation phenomena discovered by Professor Henri Becquerel', 'share': 4}]}, {'_id': {'$oid': '6683f1b44f1b49630fc783da'}, 'year': 1902, 'category': 'peace', 'laureates': [{'firstname': 'Élie', 'surname': 'Ducommun', 'motivation': 'for his untiring and skilful directorship of the Bern Peace Bureau', 'share': 2}, {'firstname': 'Albert', 'surname': 'Gobat', 'motivation': 'for his eminently practical administration of the Inter-Parliamentary Union', 'share': 2}]}, {'_id': {'$oid': '6683f1b44f1b49630fc783db'}, 'year': 1902, 'category': 'physics', 'laureates': [{'firstname': 'Hendrik A.', 'surname': 'Lorentz', 'motivation': 'in recognition of the extraordinary service they rendered by their researches into the influence of magnetism upon radiation phenomena', 'share': 2}, {'firstname': 'Pieter', 'surname': 'Zeeman', 'motivation': 'in recognition of the extraordinary service they rendered by their researches into the influence of magnetism upon radiation phenomena', 'share': 2}]}, {'_id': {'$oid': '6683f1b44f1b49630fc783df'}, 'year': 1901, 'category': 'peace', 'laureates': [{'firstname': 'Henry', 'surname': 'Dunant', 'motivation': 'for his humanitarian efforts to help wounded soldiers and create international understanding', 'share': 2}, {'firstname': 'Frédéric', 'surname': 'Passy', 'motivation': 'for his lifelong work for international peace conferences, diplomacy and arbitration', 'share': 2}]}]
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
    return [{'_id': {'$oid': '6683f1b44f1b49630fc783b7'}, 'year': 1909, 'category': 'peace', 'laureates': [{'firstname': 'Auguste', 'surname': 'Beernaert', 'motivation': 'for their prominent position in the international movement for peace and arbitration', 'share': 2}, {'firstname': 'Paul Henri', 'surname': "d'Estournelles de Constant", 'motivation': 'for their prominent position in the international movement for peace and arbitration', 'share': 2}]}, {'_id': {'$oid': '6683f1b44f1b49630fc783b8'}, 'year': 1909, 'category': 'physics', 'laureates': [{'firstname': 'Guglielmo', 'surname': 'Marconi', 'motivation': 'in recognition of their contributions to the development of wireless telegraphy', 'share': 2}, {'firstname': 'Ferdinand', 'surname': 'Braun', 'motivation': 'in recognition of their contributions to the development of wireless telegraphy', 'share': 2}]}, {'_id': {'$oid': '6683f1b44f1b49630fc783bc'}, 'year': 1908, 'category': 'peace', 'laureates': [{'firstname': 'Klas Pontus', 'surname': 'Arnoldson', 'motivation': 'for their long time work for the cause of peace as politicians, peace society leaders, orators and authors', 'share': 2}, {'firstname': 'Fredrik', 'surname': 'Bajer', 'motivation': 'for their long time work for the cause of peace as politicians, peace society leaders, orators and authors', 'share': 2}]}, {'_id': {'$oid': '6683f1b44f1b49630fc783be'}, 'year': 1908, 'category': 'medicine', 'laureates': [{'firstname': 'Ilya', 'surname': 'Mechnikov', 'motivation': 'in recognition of their work on immunity', 'share': 2}, {'firstname': 'Paul', 'surname': 'Ehrlich', 'motivation': 'in recognition of their work on immunity', 'share': 2}]}, {'_id': {'$oid': '6683f1b44f1b49630fc783c8'}, 'year': 1906, 'category': 'medicine', 'laureates': [{'firstname': 'Camillo', 'surname': 'Golgi', 'motivation': 'in recognition of their work on the structure of the nervous system', 'share': 2}, {'firstname': 'Santiago', 'surname': 'Ramón y Cajal', 'motivation': 'in recognition of their work on the structure of the nervous system', 'share': 2}]}, {'_id': {'$oid': '6683f1b44f1b49630fc783db'}, 'year': 1902, 'category': 'physics', 'laureates': [{'firstname': 'Hendrik A.', 'surname': 'Lorentz', 'motivation': 'in recognition of the extraordinary service they rendered by their researches into the influence of magnetism upon radiation phenomena', 'share': 2}, {'firstname': 'Pieter', 'surname': 'Zeeman', 'motivation': 'in recognition of the extraordinary service they rendered by their researches into the influence of magnetism upon radiation phenomena', 'share': 2}]}]
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