"""
BootCamp 2024
Jour 3
Partie 2
"""
from csv import excel

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
    return bs_obj.title.string

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
    :return: list[str
    """
    base_obj = create_bs_obj(file)
    return [str(header) for header in base_obj.find_all(re.compile(r'h[1-100]'))]

# ------------------------------
def extract_table(file: str) -> list[dict]:
    """
    Extract the table from the html file
    :param file: str
    :return: list[dict]
    """
    base_obj = create_bs_obj(file)
    table = base_obj.find("table")
    y = table.find_all("th")
    x = table.find_all("tr")[1:]
    result = []
    for line in x:
        data_line = line.find_all("td")
        new_form_data = {}
        for c in range(len(data_line)):
            new_form_data[y[c].text]=data_line[c].text
        result.append(new_form_data)
    return result