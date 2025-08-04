from ._tool import Tool
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from pydantic import Field
from typing_extensions import TypedDict


class EmailResponse(TypedDict):
    success: bool


class EmailTool(Tool[SendGridAPIClient]):
    """Sends an email using SendGrid."""
    subject: str
    html_content: str
    from_email: str = Field(default="oscar.bahamonde@pucp.pe")
    to_emails: str = Field(default="oscar.bahamonde@pucp.pe")

    def __load__(self) -> SendGridAPIClient:
        return SendGridAPIClient(os.environ["SENDGRID_API_KEY"])

    def run(self):
        """Sends the email."""
        client = self.__load__()
        response = client.send(
            Mail(
                subject=self.subject,
                html_content=self.html_content,
                from_email=self.from_email,
                to_emails=self.to_emails,
            )
        )
        return EmailResponse(success=response.status_code == 202)
