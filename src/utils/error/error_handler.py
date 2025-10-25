from fastapi import Request
from fastapi.responses import JSONResponse
from .errors import BaseError

async def custom_error_handler(request:Request, exc:BaseError):
    if exc.is_operational:
        return JSONResponse(
            status_code=exc.status_code,
            content={
                'err_type': exc.type,
                'err_msg': exc.detail,
                'path': request.url.path
            }
        )
    
    return JSONResponse(
        status_code=500,
        content={
            'err_msg': 'internal server error'
        }
    )