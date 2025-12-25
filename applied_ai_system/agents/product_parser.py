from models.product_model import ProductModel
class ProductParsingAgent:
    def run(self, raw_data: dict) -> ProductModel:
        return ProductModel(**raw_data)