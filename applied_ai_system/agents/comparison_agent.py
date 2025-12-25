from models.product_model import ProductModel
class ComparisonLogicAgent:
    def create_fictional_product(self):
        return ProductModel(
            product_name="RadiantC Serum X",
            concentration="8%",
            skin_type=["All"],
            key_ingredients=["Vitamin C"],
            benefits=["Brightening"],
            how_to_use="Apply once daily",
            side_effects="None reported",
            price=799
        )