"""
This file contains settings and constants used throughout the project, such as API keys and default model configurations.
"""
import os
from dotenv import load_dotenv
load_dotenv() 
# Settings
DEFAULT_MODEL = "mistral-medium-latest" # "mistral-large-latest" after testing

# API
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")