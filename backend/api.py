from fastapi import FastAPI
import requests

# Local Imports
import spoonacular

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/getrecipes/{query}")
def get_recipes(query):
    """Returns a list of recipe results based on the query. 
    
    Arguments:
    query -- a recipe query string
    """

    recipes = spoonacular.search_recipes(query)

    # Return the data if there are results
    if recipes:
        return {"msg": recipes}
    return {"msg": "none"}
    


