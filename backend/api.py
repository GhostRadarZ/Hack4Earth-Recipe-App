from fastapi import FastAPI
import requests

# Local Imports
import spoonacular

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

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

@app.get("/food/upc/{upc}")
def get_product_by_upc(upc: str) -> dict:
    """ Returns data about the food product the UPC identifies.

    Arguments:
    upc -- the twelve digit UPC code 
    """

    product = spoonacular.get_grocery_by_upc(upc)
    return product


    


