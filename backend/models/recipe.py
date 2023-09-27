""" A Schema for a Recipe """

from pydantic import BaseModel, Field
from typing import Optional, List

from .ingredient import Ingredient

class Recipe(BaseModel):
    spn_id: Optional[int]
    name: str = Field(..., max_length = 100)
    ingredients: List[Ingredient]
    # preparation_minutes: int = Field(..., ge=0)
    # cooking_minutes: int = Field(..., ge=0)
    total_minutes: int = Field(..., ge=0)
    servings: int = Field(..., ge=0)
    instructions: Optional[str] = None
    summary: Optional[str] = None
    image: Optional[str] = None

    @classmethod
    def from_external_data(cls, data):
        """ Processes spoonacular data and creates a Recipe 
        
        Arguments:
        data -- the data that the spoonacular API returned
        """

        # Process the ingredients
        ingredients = []
        for ingredient in data["extendedIngredients"]:

            measure_data = ingredient["measures"]["metric"]

            ing_data = {
                "spn_id": ingredient.get("id"),
                "name": ingredient.get("name"),
                "amount": measure_data.get("amount", 0),
                "unit": measure_data.get("unitShort")
            }

            ingredients.append(Ingredient(**ing_data))

        processed_data = {
            "spn_id": data.get('id'),
            "name": data.get('title'),
            "ingredients": ingredients,
            "total_minutes": data.get("readyInMinutes", 0),
            "servings": data.get("servings", 0),
            "instructions": data.get("instructions", None),
            "summary": data.get("summary", None),
            "image": data.get("image", None)
        }

        return cls.parse_obj(processed_data)