import json
from agents.orchestrator import OrchestratorAgent
with open("data/input_product.json") as f:
    input_data = json.load(f)
OrchestratorAgent().run(input_data)
print("✅ System executed successfully")