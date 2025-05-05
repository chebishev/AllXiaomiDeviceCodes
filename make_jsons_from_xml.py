import requests
import xml.etree.ElementTree as ET
from scraper import get_last_breadcrumb
from json_data import write_dictionary_to_json
from fix_model_names import correct_market_names

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
            # filter the list through the correct_market_names function
            corrected_list = correct_market_names(last_breadcrumb_list)
            # make codename as key and last breadcrumb list as value
            codenames_as_keys[codename] = corrected_list
            # make market names as keys and codename as value
            for i in range(len(corrected_list)):
                market_names_as_keys[corrected_list[i]] = codename

write_dictionary_to_json("codenames_as_keys.json", codenames_as_keys)
write_dictionary_to_json("market_names_as_keys.json", market_names_as_keys)
