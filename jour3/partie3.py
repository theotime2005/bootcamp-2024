"""
BootCamp 2024
Jour 3
Partie 3
"""
import requests
from bs4 import BeautifulSoup

from html_utils import fetch_html

def find_links_in_paragraphs(url: str) -> list[str] :
    """
    This function takes a url and return the links list in the page
    :param url: str
    :return: list[str
    """
    try:
        response = requests.get(url)
        doc = BeautifulSoup(response.text, "html.parser")
        paragraphes = doc.find_all("p")
        result = []
        for paragraphe in paragraphes:
            for link in paragraphe.find_all("a", href=True):
                result.append(link['href'])
        return result
    except requests.exceptions.ConnectionError:
        return []


# ------------------------------
def download_images(url: str, folder: str, max: int | None = None):
    """
    This function takes a url and download the images in the page
    :param url: str
    :param folder: str
    :param max: int | None
    """
    try:
        doc = BeautifulSoup(fetch_html(url), "html.parser")
        images = doc.find_all("img")
        base_url=url.split(":")[0]
        for image in images:
            if not image["src"].startswith("/static/"):
                download_image = fetch_html(f"{base_url}:{image['src']}")
                with open("{}/{}".format(folder, image['src'].split("/")[-1]), "w") as f:
                    f.write(download_image)
            if type(max)==int and max:
                max -= 1
            else:
                return
    except requests.exceptions.ConnectionError:
        print("Connexion error")
        return

# ------------------------------
def get_nth_wiki_link(html, nb):
    """
    Fonction pour obtenir le n-ième lien d'une page Wikipedia française.
    Elle retourne l'URL complète du lien.
    """
    soup = BeautifulSoup(html, 'html.parser')
    # Trouver tous les liens qui pointent vers d'autres pages Wikipédia
    wiki_links = [a['href'] for a in soup.find_all('a', href=True) if a['href'].startswith('/wiki/')]

    if len(wiki_links) > nb:
        return 'https://fr.wikipedia.org' + wiki_links[nb]  # Construire l'URL complète
    else:
        return None


def recursive_navigation(url, nb):
    """
    Fonction récursive pour naviguer à travers n pages Wikipédia.
    Elle retourne la liste des URLs visitées.
    """
    if nb < 0:
        return []  # Base de récursion : si n < 0, on arrête

    # Récupérer le contenu HTML de la page actuelle
    html = fetch_html(url)

    # Récupérer le n-ième lien interne vers une autre page Wikipedia
    next_url = get_nth_wiki_link(html, nb)

    if not next_url:
        return [url]  # Si aucun lien n'est trouvé, on arrête ici

    # Appel récursif en diminuant n
    return [url] + recursive_navigation(next_url, nb - 1)