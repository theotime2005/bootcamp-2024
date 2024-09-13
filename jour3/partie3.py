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
            result+=paragraphe.find_all("a")
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
        base_url="{}.org".format(url.split(".org")[0])
        for image in images:
            if image["src"].startswith("/static/"):
                download_image = fetch_html(f"{base_url}{image['src']}")
                with open("{}/{}".format(folder, image['src'].split("/")[-1]), "w") as f:
                    f.write(download_image)
            max-=1
            if max==0:
                break
    except requests.exceptions.ConnectionError:
        print("Connexion error")
        return


# ------------------------------
def recursive_navigation(url: str, nb: int) -> list[str] :
    """
    This function takes a url and return the links list in the page
    :param url: str
    :param nb: int
    :return: list[str]
    """
    try:
        doc = BeautifulSoup(fetch_html(url), "html.parser")
        links = doc.find_all("a")
        result = []
        for link in links:
            if nb>0 and link['href'].startswith("/wiki"):
                url_to_download = "{}.org".format(url.split(".org")[0])
                result+=recursive_navigation("{}{}".format(url_to_download[:-1],link["href"]), nb-1)
            result.append(link["href"])
        return result
    except requests.exceptions.ConnectionError:
        return []

# ------------------------------
