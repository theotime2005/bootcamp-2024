from pymongo import MongoClient

def prizes_per_category_basic(client: MongoClient) -> list[dict]:
    # Accéder à la collection où sont stockées les données sur les prix Nobel
    db = client["nobel"]
    collection = db["prizes"]

    # Effectuer l'agrégation pour compter les prix par catégorie
    pipeline = [
        {
            "$group": {
                "_id": "$category",  # Grouper par catégorie
                "count": {"$sum": 1}  # Compter le nombre de prix par catégorie
            }
        },
        {
            "$project": {
                "_id": 0,  # Ne pas inclure l'_id dans le résultat final
                "category": "$_id",
                "count": 1
            }
        }
    ]

    # Exécuter l'agrégation
    result = list(collection.aggregate(pipeline))

    return result

def prizes_per_category_sorted(client: MongoClient) -> list[dict]:
    # Accéder à la collection où sont stockées les données sur les prix Nobel
    db = client["nobel"]
    collection = db["prizes"]

    # Effectuer l'agrégation pour compter les prix par catégorie et trier
    pipeline = [
        {
            "$group": {
                "_id": "$category",  # Grouper par catégorie
                "count": {"$sum": 1}  # Compter le nombre de prix par catégorie
            }
        },
        {
            "$project": {
                "_id": 0,  # Ne pas inclure l'_id dans le résultat final
                "category": "$_id",
                "count": 1
            }
        },
        {
            "$sort": {
                "count": -1,  # Trier par nombre de prix Nobel décroissant
                "category": 1  # En cas d'égalité, trier par ordre alphabétique de la catégorie
            }
        }
    ]

    # Exécuter l'agrégation
    result = list(collection.aggregate(pipeline))

    return result

def prizes_per_category_filtered(client: MongoClient, nb_laureates: int) -> list[dict]:
    # Accéder à la collection où sont stockées les données sur les prix Nobel
    db = client["nobel"]
    collection = db["prizes"]

    # Effectuer l'agrégation pour filtrer et compter les prix par catégorie
    pipeline = [
        {
            "$match": {
                "laureates": {"$size": nb_laureates}  # Filtrer par nombre de lauréats
            }
        },
        {
            "$group": {
                "_id": "$category",  # Grouper par catégorie
                "count": {"$sum": 1}  # Compter le nombre de prix par catégorie
            }
        },
        {
            "$project": {
                "_id": 0,  # Ne pas inclure l'_id dans le résultat final
                "category": "$_id",
                "count": 1
            }
        }
    ]

    # Exécuter l'agrégation
    result = list(collection.aggregate(pipeline))

    return result

def prizes_per_category(client: MongoClient, nb_laureates: int) -> list[dict]:
    # Accéder à la collection où sont stockées les données sur les prix Nobel
    db = client["nobel"]
    collection = db["prizes"]

    # Pipeline d'agrégation pour filtrer, compter et trier les prix par catégorie
    pipeline = [
        {
            "$match": {
                "laureates": {"$size": nb_laureates}  # Filtrer les prix par nombre de lauréats
            }
        },
        {
            "$group": {
                "_id": "$category",  # Grouper par catégorie
                "count": {"$sum": 1}  # Compter le nombre de prix par catégorie
            }
        },
        {
            "$project": {
                "_id": 0,  # Ne pas inclure l'_id dans le résultat final
                "category": "$_id",
                "count": 1
            }
        },
        {
            "$sort": {
                "count": -1,  # Trier par nombre de prix décroissant
                "category": 1  # Puis trier par catégorie dans l'ordre alphabétique
            }
        }
    ]

    # Exécuter l'agrégation
    result = list(collection.aggregate(pipeline))

    return result

def laureates_per_birth_country_complex(client: MongoClient) -> list[dict]:
    # Accéder à la collection où sont stockées les données sur les lauréats
    db = client["nobel"]
    collection = db["laureates"]

    # Pipeline d'agrégation
    pipeline = [
        {
            "$match": {
                "$or": [
                    {"diedCountry": {"$exists": False}},  # Les lauréats encore vivants (sans champ 'diedCountry')
                    {"$expr": {"$eq": ["$bornCountry", "$diedCountry"]}}  # Ceux morts dans leur pays de naissance
                ]
            }
        },
        {
            "$group": {
                "_id": "$bornCountry",  # Grouper par pays de naissance
                "count": {"$sum": 1}  # Compter le nombre de lauréats par pays
            }
        },
        {
            "$project": {
                "_id": 0,  # Ne pas inclure l'_id dans le résultat final
                "birthCountry": "$_id",
                "count": 1
            }
        },
        {
            "$sort": {
                "birthCountry": 1  # Trier par pays de naissance en ordre alphabétique
            }
        }
    ]

    # Exécuter l'agrégation
    result = list(collection.aggregate(pipeline))

    return result