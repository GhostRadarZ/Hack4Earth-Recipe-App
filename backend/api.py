""" Backend REST API for recipe-app """

from fastapi import FastAPI
import requests

# Local Imports
import spoonacular
from models.ingredient import Ingredient
from models.recipe import Recipe

from mongo_db import RecipeDatabase
from datetime import date

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
    insert = app.db.create(recipe)
    print(insert)

    return recipe


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


# Functions related to retrieving user's data
# -----------------------------------------------------

@app.get("/user/{user}/recipes")
def retrieve_users_recipes(user: str):
    """Retrieves a user's stored recipes. 
    
    Arguments:
    user -- username

    ! Should add a way of authentication !
    
    TO BE IMPLEMENTED
    """
    ...

@app.get("/user/{user}/ingredients")
def retrieve_users_ingredients(user: str):
    """Retrieves a user's stored ingredients .
    
    Arguments:
    user -- username

    TO BE IMPLEMENTED
    """
    ...



# Functions related to saving to database
# -----------------------------------------------------

@app.post("/user/{user}/ingredient")
def add_ingredient(user: str, ingredient: str, expiry_date: date=None):
    """ Adds an ingredient to the user's list of ingredients. 
    
    Arguments:
    user -- username
    ingredient -- query parameter, ingredient name
    expiry_date -- the date of expiry (can be none)

    Returns:
    ?

    TO BE IMPLEMENTED
    """
    ...

@app.delete("/user/{user}/ingredient")
def delete_ingredient(user: str, ingredient: str):
    """Deletes an ingredient from the user's list of ingredients
    
    Arguments:
    user -- username
    name -- the name of the ingredient to be deleted

    TO BE IMPLEMENTED
    """
    ...


@app.get("user/{user}/recipe")
def add_recipe(user: str, spn_id: int):
    """ Adds a recipe to user's recipe list given the Spoonacular id.
    
    user -- username 
    spn_id -- the spoonacular id of the recipe

    TO BE IMPLEMENTED
    """
    ...

@app.post("/user/{user}/recipe")
def create_recipe(user: str, ingredient: str):
    """Creates a custom recipe and adds it to the user's recipe list.
    
    Arguments:
    user -- username
    name -- 

    TO BE IMPLEMENTED
    """
    ...

@app.delete("/user/{user}/recipe")
def delete_recipe(user: str, id: int):
    """Deletes a recipe from the user's saved recipes. 
    
    Arguments:
    id -- the id of the recipe to be deleted

    TO BE IMPLEMENTED
    """

