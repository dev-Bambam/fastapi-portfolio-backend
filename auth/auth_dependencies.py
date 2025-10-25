from core.config import settings
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

from fastapi import Depends, status

oauth2_scheme = OAuth2PasswordBearer("/api/v1/admin/token")

def get_current_user(token: str = Depends(oauth2_scheme)):
    TOKEN_EXCEPTION = HTTPException(
        status_code=status.HTTP_403_FORBIDDEN, 
        detail="Invalid user"
    )

    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRETKEY,
            algorithms=[settings.JWT_ALGORITHM]
        )

        admin_username: str = payload.get('sub')
        if not admin_username:
            print('coming from first if')
            raise TOKEN_EXCEPTION
        
        if admin_username != settings.ADMIN_USERNAME:
            print('coming from 2nd if')
            raise TOKEN_EXCEPTION
        
    except JWTError as e:
        print(f'this is jwt error: {e} and here is the token:{token}')
        raise TOKEN_EXCEPTION
    
    return admin_username
    
