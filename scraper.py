import requests
from bs4 import BeautifulSoup

def get_last_breadcrumb(url):
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
        # Split and strip extra whitespace and non-breaking spaces from each name
        return [part.strip().replace('\xa0', '') for part in raw.split(" / ")]
    return None
