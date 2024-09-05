"""
BootCamp 2024
Jour 3
Partie 1
"""

import requests

def get_request(url: str) -> (int, str):
    """
    Do a request and return a tuple with status code and json data
    :param url: str
    :return: tuple(int, str)
    """
    response = requests.get(url)
    return (response.status_code, response.json())

# ------------------------------
def get_countries_info(country_codes: list, info: list) -> (int, str):
    """
    Get info about countries
    :param country_codes: list
    :param info: list
    :return: (int, str)
    """
    request_url = "https://restcountries.com/v3.1/alpha?codes="
    for code in country_codes:
        request_url+=f"{code},"
    request_url=request_url[:-1]
    response = requests.get(request_url)
    data = response.json()
    result = []
    for country in data:
        for information in info:
            if country.get(information):
                result.append({information:country[information]})
    return (response.status_code, result)

# ------------------------------
def handle_request_status(url: str) -> int | str :
    """
    Handle request status
    :param url: str
    :return: int | str
    """
    try:
        req = requests.post(url)
        req.raise_for_status()
        if req.status_code==200:
            return req.status_code
    except requests.exceptions.HTTPError as http_err:
        return http_err

# ------------------------------
def send_query_parameters(params: dict) -> dict:
    """
    Send query parameters
    :param params: dict
    :return: dict
    """
    response = requests.get("https://httpbin.org/response-headers", params=params)
    return response.headers

def send_headers(headers: dict) -> str:
    """
    Send headers
    :param headers: dict
    :return: str
    """
    response = requests.get("https://httpbin.org/headers", headers=headers)
    return response.json()['headers']