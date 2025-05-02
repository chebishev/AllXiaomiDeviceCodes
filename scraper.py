import requests
from bs4 import BeautifulSoup

def get_last_breadcrumb(url):
    """
    Get the last breadcrumb from the Xiaomi Mi ROM website.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    breadcrumbs = soup.find_all("li", class_="breadcrumb-item")
    if breadcrumbs:
        return breadcrumbs[-1].text.strip()
    return None
