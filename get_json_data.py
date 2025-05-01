import requests

URL = "https://raw.githubusercontent.com/XiaomiFirmwareUpdater/xiaomi_devices/gsmarena/gsmarena_codenames.json"


data = requests.get(URL).json()