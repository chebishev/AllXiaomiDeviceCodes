from json_data import get_json_data
from prettytable import PrettyTable
from fix_model_names import correct_market_name

"""This script is only used in 
https://replit.com/@chebishev/AllXiaomiDeviceCodes
It is console version and is not used in the main.py file.
It provides up to date information directly from
JSON file stored in the github repository of @XiaomiFirmwareUpdater."""

table = PrettyTable(["Device", "Codename"])

for market_name, codename in get_json_data("market_names_as_keys.json").items():
    table.add_row([market_name, codename])

table.sortby = "Device"

print(table)
