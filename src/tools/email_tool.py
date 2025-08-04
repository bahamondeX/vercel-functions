from ._tool import Tool
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dataclasses import dataclass, field

@dataclass
class Email(Mail):
	subject: str
	html_content: str
	from_email: str = field(default="oscar.bahamonde@pucp.pe")
	to_emails: str = field(default="oscar.bahamonde@pucp.pe")


class EmailTool(Tool[SendGridAPIClient]):
	"""Sends an email using SendGrid."""
	message: Email

	def __load__(self) -> SendGridAPIClient:
		return SendGridAPIClient(os.environ["SENDGRID_API_KEY"])

	def run(self):
		"""Sends the email."""
		client = self.__load__()
		response = client.send(self.message)
		return response