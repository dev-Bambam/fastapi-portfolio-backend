from fastapi import APIRouter, Depends
from .profile_schemas import ProfileRead, ProfileBase, ProfileUpdate
from .profile_service import create_or_update_profile, get_profile_service
from sqlalchemy.orm import Session
from core.db import get_db

router = APIRouter(prefix='/profile', )

@router.post('/', response_model=ProfileRead)
async def create_profile(profile_data:ProfileBase, db:Session = Depends(get_db)):
    profile  = create_or_update_profile(db, profile_data)
    return profile

@router.put('/', response_model=ProfileRead)
async def update_profile(profile_data: ProfileUpdate, db:Session = Depends(get_db)):
    profile = create_or_update_profile(db, profile_data)
    return profile

@router.get('/', response_model=ProfileRead)
async def retrieve_profile(db:Session = Depends(get_db)):
    profile = get_profile_service(db)
   
    return profile