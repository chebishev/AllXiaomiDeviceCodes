from fastapi import FastAPI, HTTPException
from json_data import get_json_data

description = """
    All Xiaomi mobile devices codenames API.
    This API provides up to date information directly from JSON file 
    stored in the github repository of @XiaomiFirmwareUpdater.
    """

app = FastAPI(
    title="All Xiaomi mobile devices codenames",
    description=description,
    summary="API with all Xiaomi mobile devices codenames and market names.",
    version="0.1.0",
    contact={
        "name": "Atanas Chebishev",
        "url": "https://chebishev.github.io/",
        "email": "atanas.chebishev@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "identifier": "MIT",
    },
)

tags_metadata = [
    {
        "name": "Get Device by market name",
        "description": "Get information about all Xiaomi mobile devices by market name.",
    },
    {
        "name": "Get Device by codename",
        "description": "Get information about all Xiaomi mobile devices by codename.",
    },
    {
        "name": "All Xiaomi mobile devices",
        "description": "Get information about all Xiaomi mobile devices.",
    },
    {
        "name": "Xiaomi mobile devices codenames",
        "description": "Get information about Xiaomi mobile devices codenames.",
    },
]

market_name_as_key = get_json_data("market_names_as_keys.json")
codename_as_key = get_json_data("codenames_as_keys.json")


@app.get("/all_devices_by_market_name", tags=["Devices by market name"])
async def get_all_devices():
    """
    Retrieve all devices by their market name.
    """
    return market_name_as_key

@app.get("/all_devices_by_codename", tags=["Devices by codename"])
async def get_all_codenames():
    """
    Retrieve all devices by their codename.
    """
    return codename_as_key

@app.get("/device_by_market_name/{market_name}", tags=["Get Device by market name"])
async def get_device_by_market_name(market_name: str):
    """
    Retrieve an item by its market name.

    - **market_name**: The name that we all know (Xiaomi 11, Redmi 2, Poco F3 GT, etc.).
    Please use the correct market name. It is case sensitive!

    Returns the item's codename, otherwise raises a not found error.
    """
    
    if market_name in market_name_as_key:
        return {market_name: market_name_as_key[market_name]}
    else:
        raise HTTPException(status_code=404, detail="Device not found")
    
    # TODO: add proper 404 exception with description and status code


@app.get("/device_by_codename/{codename}", tags=["Get Device by codename"])
async def get_device_by_codename(codename: str):
    """
    Retrieve an item by its codename.

    - **codename**: The name that Xiaomi uses to identify the device or set of devices.
    Please use the correct codename. It is case sensitive!

    Returns the item's market name, otherwise raises a not found error.
    """
    current_codename = codename.lower()
    if current_codename in codename_as_key:
        return {codename: codename_as_key[current_codename]}
    else:
        raise HTTPException(status_code=404, detail="Device not found")
    

# TODO: Add endpoint with link to device roms

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
