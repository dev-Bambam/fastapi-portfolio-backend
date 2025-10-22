from fastapi import APIRouter
from auth.auth import router as AuthRouter

router = APIRouter()

router.include_router(AuthRouter)