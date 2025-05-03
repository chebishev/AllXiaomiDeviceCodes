import json



def get_json_data(file_name):
    """
    Fetches JSON data from the specified URL.
    Returns:
        dict: The JSON data as a dictionary.
    """
    
    with open(file_name, "r") as file:
        data = json.load(file)

    return data

# print(get_json_data("codenames_as_keys.json"))
# print(get_json_data("market_names_as_keys.json"))
