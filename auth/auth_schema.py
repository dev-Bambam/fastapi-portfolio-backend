from pydantic import BaseModel

class User(BaseModel):
    username:str

class LoginData(User):
    password: str

class LoginResponse(BaseModel):
    token:str