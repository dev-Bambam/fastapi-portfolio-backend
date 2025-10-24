from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from .profile_model import Profile
from .profile_schemas import (
    ProfileBase,
    ProfileUpdate
)

def create_profile(db:Session, profile: ProfileBase) -> Profile:
    try:
        profile_dict = profile.model_dump()
        new_profile = Profile(**profile_dict)

        db.add(new_profile)
        db.commit()
        db.refresh(new_profile)

    except IntegrityError as e:
        db.rollback()
        print(f' integrity error occured: {e}')
        raise Exception('profile already exist')
    
    except SQLAlchemyError as e:
        db.rollback()
        print(f'SQLAlchemy error:{e}')
        raise Exception('A generic DB error occured')
    
    return new_profile
    
def get_profile(db:Session) -> Profile | None:
    query = select(Profile).where(Profile.id == 1)
    profile = db.scalar(query)

    return profile
    
def update_profile(db:Session, profile:ProfileUpdate) -> Profile:
    profile_to_update = get_profile(db)
    if not profile_to_update:
        raise Exception('Profile not found')
    
    try:
        update_data = profile.model_dump(exclude_unset=True)

        # Use setattr to update attributes dynamically
        for key, value in update_data.items():
            setattr(profile_to_update, key, value)
        
        # Commit and refresh
        db.add(profile_to_update)
        db.commit()
        db.refresh(profile_to_update)

        return profile_to_update
    except SQLAlchemyError as e:
        db.rollback()
        print(f'Generic DB error: {e}')

def delete_profile(db:Session) -> bool:
    profile_to_delete = get_profile(db)

    if not profile_to_delete:
        return False
    
    try:
        db.delete(profile_to_delete)
        db.commit()
        return True
    except SQLAlchemyError as e:
        db.rollback()
        print(f'Generic DB Error: {e}')
