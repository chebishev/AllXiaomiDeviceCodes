import requests
from prettytable import PrettyTable

url = "https://raw.githubusercontent.com/XiaomiFirmwareUpdater/xiaomi_devices/gsmarena/gsmarena_codenames.json"
data = requests.get(url).json()

table = PrettyTable(["Device", "Codename"])

for market_name, codenames in data.items():
    if market_name.startswith("Xiaomi "):
        sub_name = market_name[7:]
        if sub_name.startswith(("Mi ", "Redmi ", "Poco", "Pocophone")):
            market_name = sub_name

    table.add_row([market_name, codenames[0]])

table.sortby = "Device"

# Write to file
with open("xiaomi_devices.txt", "w", encoding="utf-8") as f:
    f.write(str(table))
