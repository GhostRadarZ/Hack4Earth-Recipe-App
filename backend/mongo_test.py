from mongo_db import RecipeDatabase

this = RecipeDatabase()
# This function is already called on initialization 
# this._connect()

# Create a recipe
doc = this.create({
    "id": 32056,
    "name": "macaroni and cheese",
    "image": "macaroni-and-cheese.png"
  }, "recipes")

# Read the given recipe 
this.read(doc.inserted_id, "recipes")

# Delete the given recipe
this.delete(doc.inserted_id, "recipes")

# try to read the given recipe 
# still reading when document was deleted?
doc1 = this.read(doc.inserted_id, "recipes")
print(doc1)

# create a new recipe
this.create({
    "id": 32005,
    "name": "macaroni and cheee",
    "image": "macaroni-and-cheese.png"
  }, "recipes")