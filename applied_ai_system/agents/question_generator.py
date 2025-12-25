class QuestionGenerationAgent:
    def run(self, product):
        return {
            "informational": [
                f"What is {product.product_name}?",
                "What are the key ingredients?"
            ],
            "usage": [
                "How should I apply this product?",
                "When should I use it?"
            ],
            "safety": [
                "Are there any side effects?",
                "Is it suitable for my skin type?"
            ],
            "pricing": [
                "What is the price of this product?"
            ],
            "comparison": [
                "How does this compare to other products?"
            ]
        }