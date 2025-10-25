from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from .profile_model import Profile
from .profile_schemas import (
    ProfileBase,
    ProfileUpdate
)


def create_profile(db:Session, profile: ProfileBase) -> Profile:
    profile_dict = profile.model_dump()
    new_profile = Profile(**profile_dict)

    try:
        db.add(new_profile)
        db.commit()
        db.refresh(new_profile)
    except IntegrityError as e:
        db.rollback()
        raise e
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    
    return new_profile
    
def get_profile(db:Session) -> Profile | None:
    query = select(Profile).where(Profile.id == 1)
    profile = db.scalar(query)
    
    return profile
    
def update_profile(db:Session, profile:ProfileUpdate) -> Profile:
    profile_to_update = get_profile(db)
    update_data = profile.model_dump(exclude_unset=True)
    # Use setattr to update attributes dynamically
    for key, value in update_data.items():
        setattr(profile_to_update, key, value)

    try:
        # Commit and refresh
        db.add(profile_to_update)
        db.commit()
        db.refresh(profile_to_update)

        return profile_to_update
    except SQLAlchemyError as e:
        db.rollback()
        raise e

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
        raise e
