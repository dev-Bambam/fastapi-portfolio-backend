from jose import jwt
from core.config import settings
from datetime import timedelta, datetime

def get_token(payload:dict) -> str:
    expire = datetime.now() + timedelta(minutes=settings.JWT_ACCESS_TOKEN_EXP_MINS)

    payload.update({'exp':expire})
    token = jwt.encode(
        payload,
        settings.JWT_SECRETKEY,
        settings.JWT_ALGORITHM
    )

    return token