from fastapi import FastAPI
from route import app_router
app = FastAPI()

app.include_router(app_router)