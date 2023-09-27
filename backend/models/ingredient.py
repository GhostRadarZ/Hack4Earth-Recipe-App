""" A Schema for an Ingredient """

from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import date

class Ingredient(BaseModel):
    spn_id: Optional[int]
    name: str = Field(..., max_length=50)
    amount: float = Field(..., ge=0)
    unit: Optional[str]
    expiry_date: Optional[date] = None

    @classmethod
    def from_external_data(cls, data):
        """ Processes spoonacular data and creates an Ingredient
        
        Arguments:
        data -- the data that the spoonacular API returned.
        """

        processed_data = {
            "spn_id": data["id"],
            "name": data["name"],
            "amount": data.get("amount", 0),
            "unit": data.get("unit", None)
        }

        return cls.parse_obj(processed_data)



