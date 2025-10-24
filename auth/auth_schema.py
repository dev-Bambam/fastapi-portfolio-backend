from pydantic import BaseModel

# Simplified Login Data - Defines the expected input JSON structure
class LoginData(BaseModel):
    username: str
    password: str

# Schema for the JWT response
class LoginResponse(BaseModel):
    access_token: str
    token_type: str = 'bearer'
