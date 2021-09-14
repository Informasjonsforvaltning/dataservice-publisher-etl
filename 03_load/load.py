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
INPUT_FILE = env.get("INPUT_FILE")


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


def delete_catalog(access_token, catalog) -> bool:
    """Tries to delete the catalog."""
    headers = {
        "Authorization": f"Bearer {access_token}",
    }

    url = catalog["identifier"]
    response = requests.delete(url, headers=headers)
    if response.status_code == 204:
        print(f"Deleted catalog {url}")
        return True
    elif response.status_code == 404:
        print(f"Catalog {url} does not exist. Safe to proceed")
        return True
    else:
        logging.error(f"Unsuccessful, status_code: {response.status_code}")
        # msg = json.loads(response.content)["msg"]
        # logging.error(f"Unsuccessful, msg : {msg}")
        logging.error(response.content)
    return False


def load_catalog(access_token, catalog) -> bool:
    """Loads the catalog and returns True if successful."""
    url = f"{DATASERVICE_PUBLISHER_HOST_URL}/catalogs"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}",
    }

    response = requests.post(url, json=catalog, headers=headers)
    if response.status_code == 200:
        print(
            f"loaded from file {json_file.name}",
        )
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
        with open(INPUT_FILE) as json_file:
            catalog = json.load(json_file)
            delete_catalog(access_token, catalog)
            result = load_catalog(access_token, catalog)
            if result:
                print(f"Successfully loaded content of {INPUT_FILE}.")
