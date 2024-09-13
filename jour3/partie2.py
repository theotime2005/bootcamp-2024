"""
BootCamp 2024
Jour 3
Partie 2
"""
import re

import bs4
from bs4 import BeautifulSoup

def create_bs_obj(file: str) -> BeautifulSoup:
    """
    Create a beautifulsoup object from a html file
    :param file: str
    :return: BeautifulSoup
    """
    with open(file, "r") as f:
        return BeautifulSoup(f, "html.parser")

# ------------------------------
def find_title(file: str) -> str:
    """
    Find the title of the html file
    :param file: str
    :return: str
    """
    bs_obj = create_bs_obj(file)
    return bs_obj.title.string.text

# ------------------------------
def find_paragraphs(file: str) -> list[str]:
    """
    Find all the paragraphs of the html file
    :param file: str
    :return: list[str]
    """
    base_obj = create_bs_obj(file)
    return [str(paragraphe) for paragraphe in base_obj.find_all("p")]

# ------------------------------
def find_links(file: str) -> list[str]:
    """
    Find all the links content of the html file
    :param file: str
    :return: list[str
    """
    base_obj = create_bs_obj(file)
    return [link['href'] for link in base_obj.find_all("a")]

# ------------------------------
def find_elements_with_css_class(file: str, class_name: str) -> list[str]:
    """
    Find all the elements with a specific class name
    :param file: str
    :param class_name: str
    :return: list[str
    """
    base_obj = create_bs_obj(file)
    return [str(element) for element in base_obj.find_all(class_=class_name)]

# ------------------------------
def find_headers(file: str) -> list[str]:
    """
    Return all headings
    :param file: str
    :return: list[str)
    """
    base_obj = create_bs_obj(file)
    return [header.text for header in base_obj.find_all(re.compile(r'h[1-6]'))]

# ------------------------------
def extract_table(file: str) -> list[dict]:
    """
    Extract the table from the HTML file and return a list of dictionaries.
    Each dictionary represents a fruit with its name, color, and price.

    :param file: str, path to the HTML file
    :return: list[dict], list of dictionaries with keys 'name', 'color', and 'price'
    """
    base_obj = create_bs_obj(file)
    table = base_obj.find("table")
    headers = [th.text.strip() for th in table.find_all("th")]  # Getting column headers
    rows = table.find_all("tr")[1:]  # Skipping the header row

    result = []
    for row in rows:
        data_line = row.find_all("td")
        fruit_data = {}

        for c in range(len(data_line)):
            key = headers[c].lower().strip()  # Normalize keys to lowercase and strip spaces
            value = data_line[c].text.strip()  # Remove extra spaces from values

            # Convert price to float if the key is 'price'
            if key == 'price':
                value = float(value.replace(',', '.').replace('$', '').strip())

            fruit_data[key] = value

        result.append(fruit_data)

    return result