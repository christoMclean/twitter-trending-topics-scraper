thonimport json
from pathlib import Path

class Settings:
    proxy: str | None = None
    timeout: int = 10

    @classmethod
    def load(cls):
        example_path = Path(__file__).with_name("settings.example.json")

        if example_path.exists():
            with open(example_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                cls.proxy = data.get("proxy")
                cls.timeout = data.get("timeout", 10)

        return cls