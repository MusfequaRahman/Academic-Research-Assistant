import os
from dataclasses import dataclass
from typing import List, Dict


@dataclass
class ResearchConfig:
    """Configuration for research parameters"""
    max_papers: int = 7
    min_year: int = 2020
    preferred_sources: List[str] = None
    output_format: str = "markdown"

    def __post_init__(self):
        if self.preferred_sources is None:
            self.preferred_sources = [
                "arxiv",
                "ieee",
                "acm",
                "springer",
                "elsevier",
                "google scholar"
            ]


class APIKeys:
    """Manage API keys"""

    @staticmethod
    def validate_keys():
        """Check if required API keys are present"""
        required_keys = {
            "GEMINI_API_KEY": os.getenv("GEMINI_API_KEY"),
            "SERPER_DEV_API_KEY": os.getenv("SERPER_DEV_API_KEY")
        }

        missing_keys = [key for key, value in required_keys.items() if not value]

        if missing_keys:
            print(f"❌ Missing API keys: {', '.join(missing_keys)}")
            print("\nPlease set them in your .env file:")
            for key in missing_keys:
                print(f"{key}=your_api_key_here")
            return False

        print("✅ All API keys found")
        return True

