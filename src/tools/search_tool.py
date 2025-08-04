import typing as tp
from httpx import Client	
from ._tool import Tool, JSONContent
from pydantic import Field
import os


class SearchTool(Tool[Client]):
    """Uses Google PSE to search for unknown information. Or real time information."""
    query: str = Field(description="The query to search for.")

    def __load__(self) -> Client:
        return Client()

    def run(self) -> JSONContent:
        """Executes a Google Custom Search using the provided query and returns the JSON results."""
        with self.__load__() as client:
            response = client.get(
                f"https://www.googleapis.com/customsearch/v1?key={os.getenv('SEARCH_ENGINE_API_KEY')}&cx={os.getenv('SEARCH_ENGINE_ID')}&q={self.query}"
            ).json()
        return JSONContent(type="json", content=response["items"])
