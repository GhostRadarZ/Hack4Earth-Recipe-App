""" Database connection with MongoDB 

PyMongo Docs:
https://pymongo.readthedocs.io/en/stable/tutorial.html
"""
import pymongo
from pymongo import MongoClient


client = MongoClient("mongodb://root:pswd@mongo:27017/")

db = client["recipe_management"]

collection_recipes = db.recipes

collection_ingredients = db.ingredients

print("hello")

print(db.list_collection_names())

print("bye")

#Function related to saving ingredients
# --------------------------------------------------

def save_ingredient(ingredient: dict)->None:
    """ Save Ingredient. 
    
    Arguments:
    ingredient -- a dictionary {id,name,image}
    """
    insert = collection_ingredients.insert_one(ingredient)

    print(insert.inserted_id)

def save_recipes(recipe: dict)->None:
    """ Save recipe. 
    
    Arguments:
    recipe -- a dictionary
            name: str
            ingredients: List[str]
            preparation_minutes: int
            cooking_minutes: int
            total_minutes: int
            servings: int
            instructions: str
            summary: str
    """
    insert = collection_recipes.insert_one(recipe)

    print(insert.inserted_id)



