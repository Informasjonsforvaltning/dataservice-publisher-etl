import json
import logging
from os import environ as env
import requests

from dotenv import load_dotenv

# Get environment
load_dotenv()
DATASERVICE_PUBLISHER_HOST_URL = env.get("DATASERVICE_PUBLISHER_HOST_URL")
ADMIN_USERNAME = env.get("ADMIN_USERNAME", "admin")
ADMIN_PASSWORD = env.get("ADMIN_PASSWORD")


def login() -> str:
    """Logs in to get an access_token."""
    url = f"{DATASERVICE_PUBLISHER_HOST_URL}/login"
    try:
        headers = {"Content-Type": "application/json"}
        data = dict(username=ADMIN_USERNAME, password=ADMIN_PASSWORD)

        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            data = response.json()
            token = data["access_token"]
            print(f"Successful login. Token >{token}<")
            return token
        else:
            logging.error(f"Unsuccessful login : {response.status_code}")
            return None
    except Exception as e:
        logging.error("Got exception", e)
    return None


def load_catalog(access_token) -> None:
    """Should return status code 201 and a valid location header."""
    url = f"{DATASERVICE_PUBLISHER_HOST_URL}/catalogs"
    with open("00_input_files/api-catalog_2.json") as json_file:
        data = json.load(json_file)
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}",
    }

    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        print("loaded from file %s", json_file.name)
        return True
    else:
        logging.error(f"Unsuccessful, status_code: {response.status_code}")
        # msg = json.loads(response.content)["msg"]
        # logging.error(f"Unsuccessful, msg : {msg}")
        logging.error(response.content)
    return False


if __name__ == "__main__":
    access_token = login()
    if access_token:
        result = load_catalog(access_token)
        if result:
            print("Successful")
