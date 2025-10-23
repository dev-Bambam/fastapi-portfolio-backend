from core.config import settings
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

from fastapi import Depends, status

oauth2_scheme = OAuth2PasswordBearer("/admin/token")

def get_current_user(token: str = Depends(oauth2_scheme)):
    TOKEN_EXCEPTION = HTTPException(
        status_code=status.HTTP_403_FORBIDDEN, 
        detail="Invalid user"
    )

    try:
        payload = jwt.decode(token, settings.JWT_SECRETKEY, settings.JWT_ALGORITHM)
        admin = payload.get("sub", "")
        if admin is not settings.ADMIN_USERNAME:
            raise TOKEN_EXCEPTION
    except JWTError:
        raise TOKEN_EXCEPTION
    
    return admin
