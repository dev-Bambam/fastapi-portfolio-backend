from fastapi import APIRouter, HTTPException, status
from core.config import settings
from .auth_schema import (
    LoginData,
    LoginResponse
)
from .auth_utils import get_token

router = APIRouter(prefix='/admin', tags=['Auth'])

@router.post('/token', response_model=LoginResponse)
async def admin_login(login_data:LoginData):
    username = login_data.username
    password = login_data.password

    if username != settings.ADMIN_USERNAME or password != settings.ADMIN_PASSWORD:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='invalid username or password'
        )
    
    payload = {'sub':settings.ADMIN_USERNAME}
    token = get_token(payload)

    return {
        'token': token
    }