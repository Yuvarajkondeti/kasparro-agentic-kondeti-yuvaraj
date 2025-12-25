import json
from agents.product_parser import ProductParsingAgent
from agents.question_generator import QuestionGenerationAgent
from agents.comparison_agent import ComparisonLogicAgent

class OrchestratorAgent:
    def run(self, input_data):
        # Parse product
        product = ProductParsingAgent().run(input_data)

        # Generate questions
        questions = QuestionGenerationAgent().run(product)

        # Create fictional product B
        product_b = ComparisonLogicAgent().create_fictional_product()

        # ---------------- FAQ PAGE ----------------
        faq_output = {
            "product_name": product.product_name,
            "faqs": questions
        }

        with open("outputs/faq.json", "w") as f:
            json.dump(faq_output, f, indent=2)

        # ---------------- PRODUCT PAGE ----------------
        product_page = {
            "product_name": product.product_name,
            "concentration": product.concentration,
            "key_ingredients": product.key_ingredients,
            "benefits": product.benefits,
            "how_to_use": product.how_to_use,
            "safety": {
                "side_effects": product.side_effects,
                "skin_type": product.skin_type
            },
            "price": product.price
        }

        with open("outputs/product_page.json", "w") as f:
            json.dump(product_page, f, indent=2)

        # ---------------- COMPARISON PAGE ----------------
        comparison_page = {
            "product_a": {
                "name": product.product_name,
                "ingredients": product.key_ingredients,
                "benefits": product.benefits,
                "price": product.price
            },
            "product_b": {
                "name": product_b.product_name,
                "ingredients": product_b.key_ingredients,
                "benefits": product_b.benefits,
                "price": product_b.price
            }
        }

        with open("outputs/comparison_page.json", "w") as f:
            json.dump(comparison_page, f, indent=2)