"""
BootCamp 2024
Jour 3
Partie 4
"""

from bs4 import BeautifulSoup
from html_utils import fetch_html

def get_one_book() -> dict:
    """
    Get a book from scraping site
    :return: dict
    """
    html_doc = BeautifulSoup(fetch_html("https://books.toscrape.com/"), "html.parser")
    book = html_doc.find("article")
    result = {}
    # Get title
    result["title"]=book.find("h3").text
    # Get rating
    result["rating"]=len(book.find_all(name="i", class_="icon-star"))
    # Get price
    result["price"]=float(book.find(name="p", class_="price_color").text[2:])
    return result

# ------------------------------
def get_one_book_complete() -> dict:
    """
    Get a book from scraping site
    :return: dict
    """
    html_doc = BeautifulSoup(fetch_html("https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"), "html.parser")
    book = html_doc.find("article")
    result = {}
    # Get title
    result["title"]=book.find("h1").text
    # Get rating
    result["rating"] = len(book.find_all(name="i", class_="icon-star"))
    # Get price
    result["price"] = float(book.find(name="p", class_="price_color").text[2:])
    # Get description
    result["description"] = book.find_all("p")[-1].text
    return result

# ------------------------------
def get_page_books(url: str | None=None) -> list[dict]:
    """
    Get all books from a page
    :param url: str
    :return: list[dict]
    """
    if not url:
        url_to_scrape = "https://books.toscrape.com/?"
    else:
        url_to_scrape = url
    home = BeautifulSoup(fetch_html(url_to_scrape), "html.parser")
    result = []
    # Get title and links
    titles = home.find_all("h3")
    for title in titles:
        link = "{}.com{}".format(url_to_scrape.split(".com")[0],title.find("a")["href"])
        html_book = BeautifulSoup(fetch_html(link), "html.parser")
        book = html_book.find("article")
        data = {}
        # Get title
        data["title"] = book.find("h1").text
        # Get rating
        data["rating"] = len(book.find_all(name="i", class_="icon-star"))
        # Get price
        data["price"] = float(book.find(name="p", class_="price_color").text[2:])
        # Get description
        for p in book.find_all("p"):
            if not p.attrs:
                data["description"] = p.text
        result.append(data)
    if not url:
        result += get_page_books("https://books.toscrape.com/catalogue/page-5.html")
    return result
