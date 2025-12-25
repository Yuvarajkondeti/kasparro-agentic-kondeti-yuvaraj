from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class ProductModel:
    product_name: str
    concentration: str
    skin_type: List[str]
    key_ingredients: List[str]
    benefits: List[str]
    how_to_use: str
    side_effects: str
    price: int