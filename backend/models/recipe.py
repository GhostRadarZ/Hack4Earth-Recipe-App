""" A Schema for a Recipe """

from pydantic import BaseModel, Field
from typing import Optional, List

class RecipeSchema(BaseModel):
    name: str
    ingredients: List[str]
    preparation_minutes: int
    cooking_minutes: int
    total_minutes: int
    servings: int
    instructions: str
    summary: str

