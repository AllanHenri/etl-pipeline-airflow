import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
SQL_DIR = DATA_DIR / "sql"

API_BASE_URL = os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com")

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "etl_db")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")

DATABESE_URL = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

USERS_RAW_FILE = RAW_DIR / "users.json"
POSTS_RAW_FILE = RAW_DIR / "posts.json"

USERS_PROCESSED_FILE = PROCESSED_DIR / "users.json"
POSTS_PROCESSED_FILE = PROCESSED_DIR / "posts.json"
