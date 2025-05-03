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


def write_dictionary_to_json(file_name, data):
    """
    Writes a dictionary to a JSON file.
    Args:
        file_name (str): The name of the JSON file to write to.
        data (dict): The dictionary to write to the JSON file.
    """
    
    with open(file_name, "w") as json_file:
        json.dump(data, json_file, indent=4)
        
# print(get_json_data("codenames_as_keys.json"))
# print(get_json_data("market_names_as_keys.json"))
