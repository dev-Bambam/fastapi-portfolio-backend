from .profile_repo import create_profile, update_profile, get_profile
from sqlalchemy.orm import Session
from .profile_schemas import ProfileBase, ProfileUpdate

def create_or_update_profile(db:Session, profile_data: ProfileBase) -> ProfileBase:
    existing_profile = get_profile(db)
    if existing_profile:
        update_payload = ProfileUpdate(**profile_data.model_dump())
        updated_profile = update_profile(db, update_payload)
        return updated_profile
    else:
        new_profile = create_profile(db, profile_data)
        return new_profile



def get_profile_service(db:Session):
    profile = get_profile(db)
    if not profile:
        raise Exception('profile not found')
    
    return profile