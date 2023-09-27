""" A MongoDB class for interfacing with the recipe-management database 

PyMongo Docs:
https://pymongo.readthedocs.io/en/stable/tutorial.html
"""

from models.ingredient import Ingredient
from models.recipe import Recipe
import os

from pydantic import BaseModel

from pymongo import MongoClient

class MongoDatabase():

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


    def create(self, model: BaseModel, collection: str=None):
        """ Saves the given model into the database. 

        specifying collection is optional if the base model is known
        (might remove this to simplify the code)

        Arguments:
        model - one of the data models we use (i.e Recipe)
        collection - the collection to store the model in

        Raises:
        ValueError -- collection arg was not provided
        """

        # Branches on the type of model (might remove this)
        if isinstance(model, Recipe):
            collection = "recipes"
        elif isinstance(model, Ingredient):
            collection = "ingredients"
        # If model is not known, rely on collection kwarg
        else: 
            if not collection:
                raise ValueError("Unknown model, the collection argument must be provided.")
            
        # Add the model to the collection
        insert = self._db[collection].insert_one(model)
        print(insert.inserted_id)

    
    def read(id: int, collection: str):
        """ reads the given document 
        
        TO BE IMPLEMENTED
        """ 
        ...

    def delete(id: int, collection: str):
        """ deletes the document with the given id in the given collection. 
        
        TO BE IMPLEMENTED
        """


   
