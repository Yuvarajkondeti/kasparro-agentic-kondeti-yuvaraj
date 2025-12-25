Multi-Agent Content Generation System
This repository contains a modular, agent-based automation system that generates structured, machine-readable content pages from a fixed product dataset. The system is designed to demonstrate:

agentic system design
deterministic automation pipelines
reusable content logic
template-based content generation
clean JSON outputs This project is implemented as part of an Applied AI engineering assignment. #Objective To design a production-style multi-agent system that:
parses structured product data
generates categorized user questions
assembles multiple content pages using templates
outputs clean JSON artifacts
avoids monolithic scripts or prompt-only solutions #System Overview The system operates as a step-based orchestration pipeline: Input Product Data
→ Product Parsing Agent
→ Question Generation Agent
→ Content Logic Blocks
→ Template Engine
→ Comparison Logic
→ JSON Outputs
Each agent has a single responsibility and communicates only via explicit inputs and outputs. #Generated Outputs The system autonomously produces the following files:
outputs/faq.json
outputs/product_page.json
outputs/comparison_page.json
All outputs are fully machine-readable JSON.
How to Run
Prerequisites
Python 3.9+
VS Code or any Python IDE
Run Steps
Clone the repository
Navigate to the project root
Run the system: python run.py
