import requests

from src.config import API_BASE_URL, USERS_RAW_FILE, POSTS_RAW_FILE
from src.utils import save_json

def fetch_endpoint(endpoint: str) -> list[dict]:
    url = f"{API_BASE_URL}/{endpoint}"
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    return response.json()

def extract_users() -> None:
    users = fetch_endpoint("users")
    save_json(users, USERS_RAW_FILE)
    print(f"Users extracted successfully to {USERS_RAW_FILE}")

def extract_posts() -> None:
    posts = fetch_endpoint("posts")
    save_json(posts, POSTS_RAW_FILE)
    print(f"Posts extracted successfully to {POSTS_RAW_FILE}")

def run_extraction() -> None:
    extract_users()
    extract_posts()

if __name__ == "__main__":
    run_extraction()