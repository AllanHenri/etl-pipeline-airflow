import pandas as pd
from sqlalchemy import create_engine, text

from src.config import DATABESE_URL, USERS_PROCESSED_FILE, POSTS_PROCESSED_FILE

def get_engine():
    return create_engine(DATABESE_URL)

def create_tables() -> None:
    users_table_sql = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        username TEXT NOT NULL,
        email TEXT NOT nULL
    );
"""

    posts_table_sql = """
    CREATE TABLE IF NOT EXISTS posts(
        id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL,
        title TEXT NOT NULL,
        body TEXT NOT NULL
    )
"""

    engine = get_engine()
    with engine.begin() as connection:
        connection.execute(text(users_table_sql))
        connection.execute(text(posts_table_sql))
    print("Tables created successfully")

def load_users() -> None:
    users_df = pd.read_csv(USERS_PROCESSED_FILE)
    engine = get_engine()

    users_df.to_sql("users", engine, if_exists="replace", index=False)
    print("Users loaded successfully into PostgreSQL.")

def load_posts() -> None:
    posts_df = pd.read_csv(POSTS_PROCESSED_FILE)
    engine = get_engine()

    posts_df.to_sql("users", engine, if_exists="replace", index=False)
    print("Posts loaded successfully into PostgreSQL.")

def run_load() -> None:
    create_tables()
    load_users()
    load_posts()

if __name__ == "__main__":
    run_load()