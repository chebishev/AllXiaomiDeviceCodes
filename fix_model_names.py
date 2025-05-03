def correct_market_name(market_name):
    """
    Corrects the market name by removing the prefix and adjusting the format.
    """
    if market_name.startswith("Xiaomi "):
        sub_name = market_name[7:]
        if sub_name.startswith(("Mi ", "Redmi ", "Poco", "Pocophone")):
            return sub_name
    return market_name

# TODO: To be removed
