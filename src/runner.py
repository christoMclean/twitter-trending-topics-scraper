thonimport json
import logging
from pathlib import Path
from extractors.twitter_parser import TwitterParser
from outputs.exporters import Exporter
from config.settings import Settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("runner")

def main():
    settings = Settings.load()

    input_path = Path("data/input.sample.json")
    if not input_path.exists():
        raise FileNotFoundError("Input file missing at data/input.sample.json")

    with open(input_path, "r", encoding="utf-8") as f:
        countries = json.load(f)

    parser = TwitterParser()
    all_results = []

    for country in countries:
        logger.info(f"Scraping country: {country}")
        trends = parser.get_trending_topics(country)
        all_results.extend(trends)

    Exporter.export_json("data/sample_output.json", all_results)
    logger.info("Scraping completed successfully.")

if __name__ == "__main__":
    main()