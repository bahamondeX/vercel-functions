from dotenv import load_dotenv
from src import SearchTool
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()


app = FastAPI()


@app.get("/search")
def search(query: str):
    return SearchTool(query=query).run()
