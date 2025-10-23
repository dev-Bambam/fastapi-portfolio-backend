from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, status
from fastapi.exceptions import HTTPException
from jose import jwt 
from core.config import settings

oauth2_scheme = OAuth2PasswordBearer('/token')

def get_current_user(token:str = Depends(oauth2_scheme)):
    payload = jwt.decode(
        token,
        settings.JWT_SECRETKEY,
        settings.JWT_ALGORITHM
    )
    username = payload.get('sub')
    if username == settings.ADMIN_USERNAME:
        return username
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Acess denied'
        )