""" A MongoDB class for interfacing with the recipe-management database 

PyMongo Docs:
https://pymongo.readthedocs.io/en/stable/tutorial.html
"""

from models.ingredient import Ingredient
from models.recipe import Recipe
import os

from typing import List

from pydantic import BaseModel

from pymongo import MongoClient

class RecipeDatabase():

    def __init__(self):
        self._set_mongo_uri()
        self._connect()

    def _set_mongo_uri(self):
        # check if the uri was set through the env variable
        # otherwise use default
        env_uri = os.getenv("RECIPE_APP_MONGO_URI")
        self._mongo_uri = env_uri if env_uri else "mongodb://root:pswd@mongo:27017/"

    def _connect(self):
        # Connects to the recipe management database
        self._client = MongoClient(self._mongo_uri)
        self._db = self._client.recipe_management
        
        # print("hellobye")
        # this = self._db.list_collection_names
        # print(this)
        # print("bye")


    def create(self, model: dict, collection: str=None) -> str:
        """ Saves the given model into the database. 

        specifying collection is optional if the base model is known
        (might remove this to simplify the code)

        Arguments:
        model - one of the data models we use (i.e Recipe)
        collection (optional) - the collection to store the model in

        Returns:
        str -- the id of the created document

        Raises:
        ValueError -- collection arg was not provided
        """

        # Branches on the type of model (might remove this)
        
            
        # Add the model to the collection
        insert = self._db[collection].insert_one(model)
        return insert

    
    def read(self, id: int, collection: str):
        """ reads the given document matching the id in the given collection
        
        TO BE IMPLEMENTED
        """ 
        ...

    def delete(self, id_del: int, collection: str):
        """ deletes the document with the given id in the given collection. 
        
        TO BE IMPLEMENTED
        """
        result = self._db[collection].delete_one({"id": id_del})
        print("deleted")

        

    def get_recipes_by_ingredients(self, ingredients: list):
        """ finds all recipes that are possible to make with the given ingredients.
        
        Arguments:
        ingredients -- a set (or list?) of ingredients

        TO BE IMPLEMENTED
        """
        ...

    def retrieve_user_recipes(self, user_id: str) -> List[Recipe]:
        """ retrieves all the stored recipes of a user
        
        TO BE IMPLEMENTED
        """
        list_of_recipes = []
        recipes = self._db["recipes"]

        for x in recipes.find():
            list_of_recipes.append(x)
        
        return list_of_recipes


    def retrieve_user_ingredients(self, user_id: str) -> List[Ingredient]:
        """ retrieves all the stored ingredients of a user. 
        
        TO BE IMPLEMENTED
        """
        ...

this = RecipeDatabase()
this._connect


this.create({
    "id": 32004,
    "name": "macaroni and cheese",
    "image": "macaroni-and-cheese.png"
  }, "recipes")

this.create({
    "id": 32005,
    "name": "macaroni and cheee",
    "image": "macaroni-and-cheese.png"
  }, "recipes")