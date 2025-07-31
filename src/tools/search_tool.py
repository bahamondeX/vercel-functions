import typing as tp
from httpx import Client	
from ._tool import Tool
import os


class SearchTool(Tool[Client]):
	"""Uses Google PSE to search for unknown information. Or real time information."""
	query:str

	def __load__(self)->Client:
		return Client()

	def run(self) -> dict[str, tp.Any]:
		with self.__load__() as client:
			return client.get(
				f"https://www.googleapis.com/customsearch/v1?key={os.getenv('SEARCH_ENGINE_API_KEY')}&cx={os.getenv('SEARCH_ENGINE_ID')}&q={self.query}"
			).json()
