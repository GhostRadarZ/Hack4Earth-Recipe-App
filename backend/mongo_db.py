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


    def create(self, data: dict, collection: str=None):
        """ Saves the given data into the database. 

        Arguments:
        data - a dict of data to be saved
        collection (optional) - the collection to store the document in

        Returns:
        The document that was created

        """
           
        # Add the model to the collection
        insert = self._db[collection].insert_one(data)
        return insert

    
    def read(self, id: int, collection: str):
        """ reads the given document matching the id in the given collection
        
        Arguments:
        id -- the id of the document 
        collection -- the collection the document is in

        Returns:
        the document retrieved from the database

        Raises:
        ValueError - if the document with the id does not exist
        """ 
        doc = self._db[collection].find_one({"_id": id})
        if doc:
            print(f'Found document with {id}')
            return doc
        
        raise ValueError(f'Document with id {id} is not in the {collection} collection')


        

    def delete(self, id_del: int, collection: str):
        """ deletes the document with the given id in the given collection. 
        
        TO BE IMPLEMENTED
        """
        result = self._db[collection].delete_one({"id": id_del})
        print(result)
        print(f"Deleted document {id_del} from {collection}")

        

    def get_recipes_by_ingredients(self, ingredients: list):
        """ finds all recipes that are possible to make with the given ingredients.
        
        Arguments:
        ingredients -- a set (or list?) of ingredients

        TO BE IMPLEMENTED
        """
        ...

    def retrieve_user_recipes(self) -> List[Recipe]:
        """ retrieves all the stored recipes of a user
        
        add user_id: str later when we have multiple users
        """
        list_of_recipes = []
        recipes = self._db["recipes"]

        for x in recipes.find():
            list_of_recipes.append(x)
        
        return list_of_recipes


    def retrieve_user_ingredients(self) -> List[Ingredient]:
        """ retrieves all the stored ingredients of a user. 
        
        add user_id: str later when we have multiple users
        """
        list_of_ingredients = []
        recipes = self._db["ingredients"]

        for x in recipes.find():
            list_of_ingredients.append(x)
         
        return list_of_ingredients

