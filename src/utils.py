import json
from pathlib import Path

def ensure_directory(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)

def save_json(data: list[dict], filepath: Path) -> None:
    ensure_directory(filepath.parent)
    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

def read_json(filepath: Path) -> list[dict]:
    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)
