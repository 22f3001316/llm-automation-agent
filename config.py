import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

class Config:
    API_TOKEN = os.getenv("AIPROXY_TOKEN", "")
    DATA_DIR = os.getenv("DATA_DIR", "/data")
    DB_PATH = os.path.join(DATA_DIR, "ticket-sales.db")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
