from .profile_repo import create_profile, update_profile, get_profile
from sqlalchemy.ext.asyncio import AsyncSession
from .profile_schemas import ProfileBase, ProfileUpdate
from src.utils.error.errors import NotFoundError

async def create_or_update_profile(db:AsyncSession, profile_data: ProfileBase) -> ProfileBase:
    existing_profile = await get_profile(db)
    if existing_profile:
        update_payload = ProfileUpdate(**profile_data.model_dump())
        updated_profile = await update_profile(db, update_payload)
        return updated_profile
    else:
        new_profile = await create_profile(db, profile_data)
        return new_profile



async def get_profile_service(db:AsyncSession):
    profile = await get_profile(db)
    if not profile:
        raise NotFoundError('profile not found')
    
    return profile