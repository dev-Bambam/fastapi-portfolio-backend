from sqlalchemy import select
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from .profile_model import Profile
from .profile_schemas import (
    ProfileBase,
    ProfileUpdate
)
from src.utils.error.errors import SQLAlchemyError as SQLAlchemyExc


async def create_profile(db:AsyncSession, profile: ProfileBase) -> Profile:
    profile_dict = profile.model_dump()
    new_profile = Profile(**profile_dict)

    try:
        db.add(new_profile)
        await db.commit()
        await db.refresh(new_profile)
    except IntegrityError as e:
        await db.rollback()
        raise SQLAlchemyExc(detail=f'{e}')
    except SQLAlchemyError as e:
        await db.rollback()
        raise SQLAlchemyExc(detail=f'{e}')
    
    return new_profile
    
async def get_profile(db:AsyncSession) -> Profile | None:
    query = select(Profile).where(Profile.id == 1)
    profile = await db.scalar(query)
    print(f'profile:{profile}')
    
    return profile
    
async def update_profile(db:AsyncSession, profile:ProfileUpdate) -> Profile:

    try:
        # Commit and refresh
        db.add(profile)
        await db.commit()
        await db.refresh(profile)

        return profile
    except SQLAlchemyError as e:
        await db.rollback()
        raise SQLAlchemyExc(detail=f'{e}')

async def delete_profile(db:AsyncSession) -> bool:
    profile_to_delete = await get_profile(db)

    if not profile_to_delete:
        return False
    
    try:
        db.delete(profile_to_delete)
        await db.commit()
        return True
    except SQLAlchemyError as e:
        await db.rollback()
        raise SQLAlchemyExc(detail=f'{e}')
