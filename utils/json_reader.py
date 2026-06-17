import json

from pathlib import Path


class JsonReader:

    def read_json(file_path: str | Path) -> dict:
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"JSON file not found: {path}")


        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)

