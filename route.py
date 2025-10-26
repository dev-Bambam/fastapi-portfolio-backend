from fastapi import APIRouter
from auth.auth import router as AuthRouter
from src.router.admin_route import router as AdminRouter
from src.router.client_route import router as ClientRouter

router = APIRouter(prefix='/api/v1')

router.include_router(AuthRouter)
router.include_router(AdminRouter)
router.include_router(ClientRouter)