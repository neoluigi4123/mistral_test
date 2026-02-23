"""
This file contains settings and constants used throughout the project, such as API keys and default model configurations. Usefull for centralizing configuration, normalizing access to variables, and keeping sensitive information out of the main codebase.
"""
import os
from dotenv import load_dotenv
load_dotenv()

# Settings
DEFAULT_MODEL = "mistral-medium-latest" # "mistral-large-latest" after testing

# API
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

#System prompt
SYSTEM_PROMPT = """
You are a helpful assistant that provides accurate and concise information to the user.
You can use the following tools to assist you in providing better responses:
- Web Search: Use this tool to search the web for up-to-date information. You can use it to find news, facts, or any information that may not be in your training data past your knowledge cutoff date (early-2025)
"""