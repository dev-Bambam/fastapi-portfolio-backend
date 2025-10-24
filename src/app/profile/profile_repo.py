from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from profile_model import Profile
from profile_schemas import (
    ProfileBase,
    ProfileRead,
    ProfileUpdate
)

def create_profile(db:Session, profile: ProfileBase) -> Profile:
    try:
        new_profile = Profile(
            full_name=profile.full_name,
            bio = profile.bio,
            social_links = profile.social_links,
            nickname = profile.nickname,
            professional_title = profile.professional_title
        )
        db.add(profile)
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
    

        

