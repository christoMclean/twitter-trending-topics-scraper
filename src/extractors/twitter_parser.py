thonimport logging
import random
from datetime import datetime
from .utils_time import utc_now_iso

logger = logging.getLogger("twitter_parser")

class TwitterParser:
    """
    Simulated scraper for trending topics.
    Replace with real scraping logic as needed.
    """

    def get_trending_topics(self, country: str):
        logger.info(f"Fetching trends for {country}")

        # Simulated trending topics list
        sample_topics = [
            "Breaking News",
            "Sports Update",
            "Celebrity Buzz",
            "Tech Trends",
            "Global Event",
        ]

        trends = []
        for topic in sample_topics:
            trends.append(
                {
                    "title": topic,
                    "tweetsCount": f"{random.randint(1,50)}K tweets",
                    "country": country,
                    "scrapedAt": utc_now_iso(),
                }
            )

        return trends