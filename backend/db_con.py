""" Database connection with MongoDB 

PyMongo Docs:
https://pymongo.readthedocs.io/en/stable/tutorial.html
"""

from pymongo import MongoClient

client = MongoClient("localhost", 27017)

db = client["recipe-management"]

collection = db.recipes