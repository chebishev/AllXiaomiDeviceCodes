import requests
import xml.etree.ElementTree as ET
from scraper import get_last_breadcrumb
import json

sitemap_url = "https://mirom.ezbox.idv.tw/sitemap.xml"
xml_data = requests.get(sitemap_url).text
root = ET.fromstring(xml_data)

codenames_as_key = {}

for url in root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc"):
    loc = url.text
    if loc.startswith("https://mirom.ezbox.idv.tw/en/phone/") and loc.count("/") == 6:
        # Format: https://mirom.ezbox.idv.tw/en/phone/{codename}/
        codename = loc.rstrip("/").split("/")[-1]
        last_breadcrumb = get_last_breadcrumb(loc)
        
        if last_breadcrumb:
            # make codename as key and last breadcrumb list as value
            # codenames_as_key[codename] = last_breadcrumb.split(" / ")
            last_breadcrub_list = last_breadcrumb.split(" / ")
            for i in range(len(last_breadcrub_list)):
                last_breadcrub_list[i] = codename

file_name = "market_names_as_keys.json"
with open(file_name, 'w') as json_file:
    json.dump(codenames_as_key, json_file, indent=4)

print(f"Data successfully written to {file_name}")