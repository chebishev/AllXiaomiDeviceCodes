from prettytable import PrettyTable
import requests
from bs4 import BeautifulSoup


def get_devices_from_url():
    """
    With BeautifulSoup, get td elements from table with id="post-5137"
    Because there are no classes near the table, we use the id attribute
    and "td" tag to get as close as possible to the elements that we need.
    They are 3 elements in total for every "tr", but we don't need the 3rd one

    :return: 3 td elements, one element per row in format:
    "Market name"
    "Code name"
    "Unnecessary data"
    """
    url = "https://xiaomiui.net/all-xiaomi-codenames-5137/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    result = soup.find(id="post-5137")
    return result.find_all('td')


# This list will contain all the data for the output table
table = [["Device", "Code name"]]
devices = get_devices_from_url()

# we are looping through all td elements
# 3 at a time and take only the first and the second ones
for index in range(0, len(devices), 3):
    code_name = devices[index + 1].text
    market_name = devices[index].text
    table.append([market_name, code_name])

# Pretty table will do the rest of the magic
# We create a new object that contains row names
tab = PrettyTable(table[0])

# after that we add the rest of the rows
tab.add_rows(sorted(table[1:]))

# print the table
print(tab)
