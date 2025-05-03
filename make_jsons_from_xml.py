import requests
import xml.etree.ElementTree as ET
from scraper import get_last_breadcrumb
import json

sitemap_url = "https://mirom.ezbox.idv.tw/sitemap.xml"
xml_data = requests.get(sitemap_url).text
root = ET.fromstring(xml_data)

codenames_as_keys = {}
market_names_as_keys = {}

for url in root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc"):
    loc = url.text
    if loc.startswith("https://mirom.ezbox.idv.tw/en/phone/") and loc.count("/") == 6:
        # Format: https://mirom.ezbox.idv.tw/en/phone/{codename}/
        codename = loc.rstrip("/").split("/")[-1]

        # Get the list of market names from the last breadcrumb
        last_breadcrumb_list = get_last_breadcrumb(loc)

        if last_breadcrumb_list:
            # make codename as key and last breadcrumb list as value
            codenames_as_keys[codename] = last_breadcrumb_list
            # make market names as keys and codename as value
            for i in range(len(last_breadcrumb_list)):
                market_names_as_keys[last_breadcrumb_list[i]] = codename

file_name = "codenames_as_keys.json"
with open(file_name, 'w') as json_file:
    json.dump(codenames_as_keys, json_file, indent=4)

print(f"Data successfully written to {file_name}")

file_name = "market_names_as_keys.json"
with open(file_name, 'w') as json_file:
    json.dump(market_names_as_keys, json_file, indent=4)

print(f"Data successfully written to {file_name}")