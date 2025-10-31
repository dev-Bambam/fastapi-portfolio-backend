from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware

from core.db import db_init
from route import router as mainRoute
from src.utils.error.error_handler import custom_error_handler, validation_exception_handler
from src.utils.error.errors import BaseError

# Init Database
# db_init()


app = FastAPI()

# Use the old @app.on_event("startup") for simplicity:
@app.on_event("startup")
async def startup_event():
    # We call the async function using await
    await db_init()

origins = [
    "*",  # CRITICAL: Allows ALL origins (domains) to access the API. Use this for testing/development.
    # In a production environment, you should replace "*" with a specific URL:
    # "https://www.your-frontend-domain.com", 
    # "http://localhost:8000", 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,             # Allow cookies and credentials to be included in requests
    allow_methods=["*"],                # Allow all standard HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],                # Allow all headers, especially required for 'Authorization' header
)

    
# Mount error handlers
app.add_exception_handler(BaseError, custom_error_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)

# Mount Route
app.include_router(mainRoute)