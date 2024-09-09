"""
BootCamp 2024
Jour 5
Partie 1
"""

import requests

def get_companies_with_name(name: str) -> list[dict]:
    try:
        url = "https://recherche-entreprises.api.gouv.fr/search"
        response = requests.get(url, params={"q": name})
        response.raise_for_status()
        data = response.json()
        result = []
        for enterprise in data['results']:
            result.append({"siren": enterprise['siren'], "nom_complet": enterprise['nom_complet'],
                           "date_creation": enterprise['date_creation']})
        return result
    except:
        return []

# ------------------------------
def get_all_companies_with_name(name: str) -> list[dict]:
    url = "https://recherche-entreprises.api.gouv.fr/search"
    result = []
    try:
        count = 1
        page_number = requests.get(url, params={"q": name}).json()['page']
        while count!=int(page_number)+1:
            response = requests.get(url, params={"q": name, "page": count})
            response.raise_for_status()
            data = response.json()
            for enterprise in data['results']:
                result.append({"siren": enterprise['siren'], "nom_complet": enterprise['nom_complet'],
                               "date_creation": enterprise['date_creation']})
            count+=1
        return result
    except:
        return []

# ------------------------------
def get_and_store_companies(filename: str, name: str):
    url = "https://recherche-entreprises.api.gouv.fr/search"
    result = []
    try:
        count = 1
        page_number = requests.get(url, params={"q": name}).json()['page']
        while count!=int(page_number)+1:
            response = requests.get(url, params={"q": name, "page": count})
            response.raise_for_status()
            data = response.json()
            for enterprise in data['results']:
                result.append({"siren": enterprise['siren'], "nom_complet": enterprise['nom_complet'],
                               "date_creation": enterprise['date_creation']})
            count+=1
        result.sort(key=lambda x: x['siren'])
        # Save in file
        with open(filename, "a") as f:
            f.write("siren,nom_complet,date_creation\n")
            for line in result:
                f.write(f"{line['siren']},{line['nom_complet']},{line['date_creation']}\n")
    except:
        return []