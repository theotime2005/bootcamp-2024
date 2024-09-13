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
    ratings= {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
    result["rating"]=ratings[book.find(name="p", class_="star-rating")["class"][1]]
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
    rating = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
    result["rating"] = rating[book.find(name="p", class_="star-rating")["class"][1]]
    # Get price
    result["price"] = float(book.find(name="p", class_="price_color").text[2:])
    # Get description
    result["description"] = book.find_all("p")[-1].text
    return result
