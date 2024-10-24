import requests
import os
from dotenv import load_dotenv
load_dotenv()
def fetch_data(animal_name):

    """
  Fetches the animals data for the animal 'animal_name'.
  Returns: a list of animals, each animal is a dictionary:
  {
    'name': ...,
    'taxonomy': {
      ...
    },
    'locations': [
      ...
    ],
    'characteristics': {
      ...
    }
  },
    """
    api_key = os.getenv("API_KEY")
    api_url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
    headers = {
        "X-Api-Key": api_key
    }
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data from the API. Status code: {response.status_code}")
        return None