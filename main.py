from dotenv import load_dotenv

load_dotenv()
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.tools.email_tool import EmailTool, EmailResponse
from src.tools.search_tool import SearchTool

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/email", response_model=EmailResponse)
def send_email(email: EmailTool):
    return email.run()


@app.post("/search")
def search(query: str):
    return SearchTool(query=query).run()
