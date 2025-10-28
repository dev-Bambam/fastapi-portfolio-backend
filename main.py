from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from core.db import db_init
from route import router as mainRoute
from src.utils.error.error_handler import custom_error_handler, validation_exception_handler
from src.utils.error.errors import BaseError

# Init Database
db_init()


app = FastAPI()

# Use the old @app.on_event("startup") for simplicity:
@app.on_event("startup")
async def startup_event():
    # We call the async function using await
    await db_init()

    
# Mount error handlers
app.add_exception_handler(BaseError, custom_error_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)

# Mount Route
app.include_router(mainRoute)