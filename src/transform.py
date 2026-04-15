import pandas as pd

from src.config import (
    USERS_RAW_FILE,
    POSTS_RAW_FILE,
    USERS_PROCESSED_FILE, 
    POSTS_PROCESSED_FILE
)

from src.utils import ensure_directory, read_json

def transform_user() ->  None:
    users_data =read_json(USERS_RAW_FILE)
    users_df = pd.DataFrame(users_data)

    users_df = users_df[["id", "name", "username", "email"]].copy()
    users_df["id"] = users_df["id"].astype(int)

    ensure_directory(USERS_PROCESSED_FILE.parent)
    users_df.to_csv(USERS_PROCESSED_FILE,index=False)
    print(f"Users transformed successfully to {USERS_PROCESSED_FILE}")

def transform_posts() -> None:
    posts_data = read_json(POSTS_RAW_FILE)
    posts_df = pd.DataFrame(posts_data)

    posts_df = posts_df[["id", "userId", "title", "body"]].copy()
    posts_df = posts_df.rename(columns={"userId": "user_id"})
    posts_df["id"] = posts_df["id"].astype(int)

    ensure_directory(POSTS_PROCESSED_FILE.parent)
    posts_df.to_csv(POSTS_PROCESSED_FILE, index=False)
    print(f"Posts tranformed successfully to {POSTS_PROCESSED_FILE}")

def run_tranformation() -> None:
    transform_user()
    transform_posts()

if __name__ == "__main__":
    run_tranformation()