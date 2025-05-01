import requests


def get_json_data():
    """
    Fetches JSON data from the specified URL.
    Returns:
        dict: The JSON data as a dictionary.
    """
    
    url = "https://raw.githubusercontent.com/XiaomiFirmwareUpdater/xiaomi_devices/gsmarena/gsmarena_codenames.json"
    # Fetch the JSON data from the URL
    data = requests.get(url).json()

    return data
