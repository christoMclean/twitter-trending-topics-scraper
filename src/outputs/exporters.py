thonimport json
import logging
from typing import List, Any

logger = logging.getLogger("exporter")

class Exporter:
    @staticmethod
    def export_json(path: str, data: List[Any]):
        try:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
            logger.info(f"Exported JSON to: {path}")
        except Exception as e:
            logger.error(f"Failed to export JSON: {e}")
            raise