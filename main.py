from fastapi import FastAPI
from core.db import db_init
from route import router as mainRoute

# Init Database
db_init()


app = FastAPI()

app.include_router(mainRoute)