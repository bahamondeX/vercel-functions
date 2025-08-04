from dotenv import load_dotenv

load_dotenv()
from fastapi import FastAPI
from src.tools.email_tool import EmailTool, Email
from src.tools.search_tool import SearchTool

app = FastAPI()


@app.post("/email")
def send_email(email: Email):
    return EmailTool(message=email).run()


@app.post("/search")
def search(query: str):
    return SearchTool(query=query).run()
