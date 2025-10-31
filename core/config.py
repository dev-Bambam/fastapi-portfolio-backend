from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    '''Loads application seeting from environmental variables'''

    # Databases
    # POSTGRES_SERVER: str
    # POSTGRES_PORT: str
    # POSTGRES_NAME: str
    # POSTGRES_USER: str
    # POSTGRES_PASSWORD: str
    DB_URL:str
    

    # This property compose the full DB_URL
    # @property
    # def DATABASE_URL(self)-> str:
    #     return(
    #         f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@"
    #         f"{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_NAME}"
    #     )

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
