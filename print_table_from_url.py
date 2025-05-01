from json_data import get_json_data
from prettytable import PrettyTable
from fix_model_names import correct_market_name

"""This script is only used in 
https://replit.com/@chebishev/AllXiaomiDeviceCodes
It is console version and is not used in the main.py file.
It provides up to date information directly from
JSON file stored in the github repository of @XiaomiFirmwareUpdater."""

table = PrettyTable(["Device", "Codename"])

for market_name, codenames in get_json_data().items():
    current_market_name = correct_market_name(market_name)
    table.add_row([current_market_name, codenames[0]])

table.sortby = "Device"

print(table)
