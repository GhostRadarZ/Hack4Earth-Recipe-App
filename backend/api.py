""" Backend REST API for recipe-app """

from fastapi import FastAPI
import requests

# Local Imports
import spoonacular
from models.ingredient import Ingredient
from models.recipe import Recipe

from mongo_db import RecipeDatabase

app = FastAPI()

@app.on_event("startup")
def connect_db():
    """ Connects to the MongoDB recipe-management database. """
    app.db: RecipeDatabase = RecipeDatabase()


@app.get("/")
async def root():
    return {"message": "Hello World"}

# Functions related to recipes
# --------------------------------------------------

@app.get("/recipes/search/{query}")
def get_recipes(query: str):
    """Returns a list of recipe results based on the query. 
    
    Arguments:
    query -- a recipe query string
    """

    recipes = spoonacular.search_recipes(query)

    # Return the data if there are results
    return recipes
    

@app.get("/recipes/info/{id}")
def get_recipe(id: int) -> Recipe:
    """ Use a recipe id to get full info about a recipe. 
    
    Arguments:
    id -- a spoonacular recipe id
    """

    result = spoonacular.get_recipe(id)
    recipe = Recipe.from_external_data(result)

    # Save recipe to database?
    print(app.db.create(recipe))


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
def search_ingredients(query: str):
    """ Search for simple whole foods. 
    
    Arguments:
    query -- a query string 
    """

    return spoonacular.search_ingredients(query)

@app.get("/food/ingredients/info/{id}")
def get_ingredient(id: int) -> Ingredient:
    """ Get an ingredient with the matching id.
    
    Arguments:
    id -- the spoonacular id of the ingredient
    """

    result = spoonacular.get_ingredient(id)
    return Ingredient.from_external_data(result)

# Functions related to displaying ingredients
# -----------------------------------------------------



# Functions related to saving ingredients to database
# -----------------------------------------------------