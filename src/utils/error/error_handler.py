from fastapi import Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from .errors import BaseError

async def custom_error_handler(request:Request, exc:BaseError):
    if exc.is_operational:
        return JSONResponse(
            status_code=exc.status_code,
            content={
                'err_type': exc.type,
                'err_msg': exc.detail,
                'path': f'{request.method} {request.url.path}',
                
            }
        )
    
    return JSONResponse(
        status_code=500,
        content={
            'err_msg': 'internal server error'
        }
    )


# --- HELPER FUNCTION FOR NORMALISED ERRORS ---
def normalize_pydantic_errors(errors: list[dict[str, any]]) -> list[dict[str, any]]:
    """
    Transforms Pydantic's verbose error list into a simplified format.
    """
    normalized = []
    for error in errors:
        # Pydantic errors have 'loc' (location) and 'msg' (message)
        field = ".".join(map(str, error.get('loc', ('body',))))
        normalized.append({
            "field": field,
            "message": error.get('msg', 'Validation failed.'),
            "input_value": error.get('input', 'N/A')
        })
    return normalized

# 2. Custom Exception Handler for Pydantic Validation Errors (HTTP 422)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """
    Overrides the default FastAPI handler for RequestValidationError (422).
    """
    # Use the helper to simplify the error list
    normalized_errors = normalize_pydantic_errors(exc.errors())
    
    # Log the verbose error for debugging purposes
    print(f"Pydantic Validation Error caught: {normalized_errors}")

    # Return a standardized JSON response
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "error_type": "VALIDATION_ERROR",
            "message": "The request body or parameters contained invalid data.",
            "errors": normalized_errors,
        },
    )