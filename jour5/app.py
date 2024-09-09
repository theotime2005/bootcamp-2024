"""
BootCamp 2024
Jour 5
App
"""
from sys import exception
from bson import json_util
from fastapi import FastAPI, HTTPException
from pymongo import MongoClient, ASCENDING

app = FastAPI()
client = MongoClient("mongodb://localhost:27017", 27017)
laureates_collection = client.nobel.laureates

@app.get("/")
def helo():
    return {"message": "Hello world, this is my first web API!"}

# ------------------- MongoDB -------------------
@app.get("/laureates")
def laureates(category=None):
    result = []
    try:
        # Construire le filtre MongoDB de manière standard
        query = {}
        if category:
            query = {"prizes.category": category}

        # Récupérer les données depuis MongoDB
        data = laureates_collection.find(query).sort("surname", ASCENDING)

        # Supprimer le champ "_id" et ajouter les lauréats à la liste de résultats
        for laureate in data:
            laureate.pop("_id")
            result.append(laureate)

        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

# ---------------------------------
