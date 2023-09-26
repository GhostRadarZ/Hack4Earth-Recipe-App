""" Backend REST API for recipe-app """

from fastapi import FastAPI
import requests

# Local Imports
import spoonacular

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# Functions related to recipes
# --------------------------------------------------

@app.get("/recipes/search/{query}")
def get_recipes(query: str) -> dict:
    """Returns a list of recipe results based on the query. 
    
    Arguments:
    query -- a recipe query string
    """

    recipes = spoonacular.search_recipes(query)

    # Return the data if there are results
    if recipes:
        return {"msg": recipes}
    return {"msg": "none"}

@app.get("/recipes/info/{id}")
def get_recipe(id: int) -> dict:
    """ Use a recipe id to get full info about a recipe. 
    
    Arguments:
    id -- a spoonacular recipe id
    """

    return spoonacular.get_recipe(id)


# Functions related to packaged grocery products
# --------------------------------------------------


@app.get("/food/product/search/{query}")
def search_food_products(query: str) -> dict:
    """ Searches for packaged food products. 
    
    Arguments:
    query -- a query string which the search is based on
    """

    return spoonacular.search_food_products(query)

@app.get("/food/product/upc/{upc}")
def get_product_by_upc(upc: str) -> dict:
    """ Returns data about the food product the UPC identifies.

    Arguments:
    upc -- the twelve digit UPC code 
    """

    product = spoonacular.get_grocery_by_upc(upc)
    return product


# Functions related to ingredients
# --------------------------------------------------

@app.get("/food/ingredient/search/{query}")
def search_ingredients(query: str) -> dict:
    """ Search for simple whole foods. 
    
    Arguments:
    query -- a query string 
    """

    return spoonacular.search_ingredients(query)










    


