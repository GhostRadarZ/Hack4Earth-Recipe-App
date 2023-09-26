"""
A Python wrapper for the Spoonacular API.

"""

import requests

# Base URL
url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/"

# Base headers with host and API key
headers = {
	"X-RapidAPI-Key": "148bc7ae7emsh9ce2312cdf4c7e7p188d53jsn20da7f80baeb",
	"X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
}


def search_recipes(query: str) -> dict:
    """Searches recipes given the query string 

    Uses the recipes/complexSearch Spoonacular endpoint 
    
    Arguments:
    query -- a recipe query string
    """

    endpoint = "recipes/complexSearch"

    query_string = {"query":query}
    response = requests.get(url + endpoint, headers=headers, params=query_string)

    return response.json()["results"]

    
