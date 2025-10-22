from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    '''Loads application seeting from environmental variables'''

    # Databases
    DATABASE_URL: str = 'sqlite:///./portfolio.db'

    # JWT Authentication
    JWT_SECRETKEY: str
    JWT_ALGORITHM: str = 'HS256'
    JWT_ACCESS_TOKEN_EXP_MINS: int = 60 * 24

    # Admin Credentials
    ADMIN_USERNAME: str 
    ADMIN_PASSWORD: str 

    class Config:
        # Pydantic will load from .env file
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()