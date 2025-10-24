from fastapi import APIRouter, Depends
from auth.auth_dependencies import get_current_user
from src.app.profile.profile_route import router as profile_route

router = APIRouter(prefix='/admin', tags=['Admin'], dependencies=[Depends(get_current_user)])

router.include_router(router=profile_route, tags=['Profile'])