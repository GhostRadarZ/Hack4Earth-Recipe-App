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

# Functions related to recipes
# --------------------------------------------------

def search_recipes(query: str) -> dict:
    """Searches recipes given the query string 

    Uses the recipes/complexSearch Spoonacular endpoint 
    
    Arguments:
    query -- a recipe query string
    """

    endpoint = "recipes/complexSearch"

    query_string = {"query":query}
    response = requests.get(url + endpoint, headers=headers, params=query_string)

    
    # Returns list of dictionaries, each have id, title and image keys
    return response.json()["results"]


def get_recipe(id: int) -> dict:
    """ Use a recipe id to get full info about a recipe. 
    
    Arguments:
    id -- a spoonacular recipe id
    """

    endpoint = f"recipes/{id}/information"

    response = requests.get(url + endpoint, headers=headers)


    return response.json()

# Functions related to packaged grocery products
# --------------------------------------------------

def search_food_products(query: str) -> dict:
    """ Searches for packaged food products. 
    
    Arguments:
    query -- a query string which the search is based on
    """

    endpoint = "food/products/search"
    data = {
        "query": query
    }

    response = requests.get(url + endpoint, params=data, headers=headers)

    return response.json()

def get_grocery_by_upc(upc: str) -> dict:
    """ Returns data about the grocery product the UPC identifies.

    Arguments:
    upc -- the twelve digit UPC code 
    """
    
    endpoint = f"food/products/upc/{upc}"

    response = requests.get(url + endpoint, headers=headers)

    return response.json()


# Functions related to ingredients
# --------------------------------------------------

def search_ingredients(query: str) -> dict:
    """ Search for simple whole foods. 
    
    Arguments:
    query -- a query string 
    """

    endpoint = "food/ingredients/search"
    data = {
        "query": query
    }

    response = requests.get(url + endpoint, params=data, headers=headers)

    results = response.json()['results']

    # Returns list of dictionaries, each have id, name and image keys
    return results

def get_ingredient(id: str) -> dict:
    """ Get ingredient information based on id.
    
    Arguments:
    id -- a valid spoonacular id for an ingredient 
    """

    endpoint = f"food/ingredients/{id}/information"
    response = requests.get(url + endpoint, headers=headers)

    print(response)

    return response.json()
    
# def create_recipe_object():
