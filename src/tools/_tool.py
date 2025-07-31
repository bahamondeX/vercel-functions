import typing as tp
import typing_extensions as tpe
from abc import ABC, abstractmethod
from groq._utils._proxy import LazyProxy
from groq.types.chat import ChatCompletionToolParam
from groq.types.shared_params import FunctionDefinition
from pydantic import BaseModel, Field

R = tp.TypeVar("R")

class AudioContent(BaseModel):
	type: tp.Literal["audio"]
	content: tp.Iterator[bytes] | bytes

class ImageContent(BaseModel):
	type: tp.Literal["image"]
	content: tp.Iterator[bytes] | bytes

class TextContent(BaseModel):
	type: tp.Literal["text"]
	content:tp.Iterator[str] | str

class JSONContent(BaseModel):
	type: tp.Literal["json"]
	content:tp.Iterator[dict[str, tp.Any]] | dict[str, tp.Any]

Content = tp.Annotated[
	tp.Union[AudioContent, ImageContent, TextContent, JSONContent],
	Field(discriminator="type"),
]


class Tool(BaseModel, LazyProxy[R], ABC):
	"""
	Base class for all tools.
	"""

	def __load__(self) -> R: ...

	def __hash__(self) -> int:
		return hash(self.model_dump_json())

	@classmethod
	def tool_definition(cls) -> ChatCompletionToolParam:
		return ChatCompletionToolParam(
			type="function",
			function=FunctionDefinition(
				name=cls.__name__,
				description=cls.__doc__ or "",
				parameters=cls.model_json_schema().get("properties", {}),
			),
		)

	@abstractmethod
	def run(self) -> Content: ...
