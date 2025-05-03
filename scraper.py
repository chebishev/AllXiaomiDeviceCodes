import requests
from bs4 import BeautifulSoup
import re
from typing import Union, List

def get_last_breadcrumb(url: str) -> Union[List[str], None]:
    """ 
    Get the last breadcrumb from the curent codename page.
    This is used to get the market names from the breadcrumb.
    params:
        url: url of the codename page
    returns:
        list: list of market names
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    breadcrumbs = soup.find_all("li", class_="breadcrumb-item")
    if breadcrumbs:
        raw = breadcrumbs[-1].text.strip()
         # Split on ' / ' or ' | ' or variants with non-breaking space
        parts = re.split(r'\s*[/|]\s*', raw.replace('\xa0', ' '))
        return [part.strip() for part in parts]
    return None
