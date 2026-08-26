import os
from crewai_tools import SerperDevTool  # type: ignore[reportMissingImports]
from dotenv import load_dotenv

load_dotenv()


def get_search_tool():

    if not os.getenv("SERPER_API_KEY"):
        raise ValueError(
            "SERPER_API_KEY is missing from .env"
        )

    return SerperDevTool(
        n=5
    )
