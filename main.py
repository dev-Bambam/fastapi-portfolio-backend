from fastapi import FastAPI
from core.db import db_init


# Init Database
db_init()


app = FastAPI()