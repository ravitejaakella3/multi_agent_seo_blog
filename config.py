import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()

# Store the Gemini API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
