correct_market_names_dict = {
    "10 Pro": "Mi Note 10 Pro",
    "10T Pro": "Mi 10T Pro",
    "12 Explorer": "Redmi Note 12 Explorer",
    "12 Pro+": "Redmi Note 12 Pro+",
    "13R Pro": "Redmi Note 13R Pro",
    "4 Pro": "Xiaomi Civi 4 Pro",
    "8A Dual": "Redmi 8A Dual",
    "9A Sport": "Redmi 9A Sport",
    "9AT": "Redmi 9AT",
    "9i": "Redmi 9i",
    "9i Sport": "Redmi 9i Sport",
    "A1+": "Redmi A1+",
    "A2+": "Redmi A2+",
    "Hypercharge (India)": "Xiaomi 11i Hypercharge 5G",
    "K40 Pro+": "Redmi K40 Pro+",
    "Plus": "Mi Pad 4 Plus",
    "Pro Max (India)": "Redmi Note 10 Pro Max (India)",
    "Pro+": "Redmi Note 11T Pro+",
    "Pro+ (China)": "Redmi Note 11 Pro+ (China)",
    "Redmi 13R 5G": "Redmi 13C 5G",
    "Ti": "Xiaom 14 Pro Titanium",
    "Ultra": "Xiaomi 11 Ultra",
    "Zoom Edition": "Redmi K30 Pro Zoom Edition",
}


def correct_market_names(market_names_list) -> list:
    """
    Refactor the market names by adding missing prefixes, missing models or just correcting the name.
    Args:
        market_names_list (list): List of market names to be checked and corrected.
    Returns:
        list: List of corrected market names.
    """
    seen_redmi_13r = False
    for index, name in enumerate(market_names_list):
        # Check if Redmi 13R 5G is twice in the list
        if name == "Redmi 13R 5G" and not seen_redmi_13r:
            seen_redmi_13r = True
            continue
        # Add Xiaomi 14T Pro to the list if Redmi K70 Ultra is in the list
        if name == "Redmi K70 Ultra" and len(market_names_list) == 1:
            return ["Redmi K70 Ultra", "Xiaomi 14T Pro"]
        if name in correct_market_names_dict:
            # If it is, replace it with the correct name
            market_names_list[index] = correct_market_names_dict[name]
    return market_names_list
