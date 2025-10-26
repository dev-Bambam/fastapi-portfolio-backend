from sqlalchemy.orm import Session
from .skill_repo import (
    create_skill, update_skill, 
    get_skill_by_id, get_skills, 
    delete_skill
)
from .skill_schemas import SkillCreate, SkillUpdate, SkillRead
from src.utils.error.errors import (
    SQLAlchemyError, NotFoundError
)

async def create_skill_service(db:Session, skill_data:SkillCreate) -> SkillRead:
    skill_dict = skill_data.model_dump() 
    try:
        new_skill = await create_skill(db, skill_dict)  
        return new_skill
    except Exception as e:
        raise SQLAlchemyError(detail=f'{e}')
    
async def update_skill_service(db:Session, skill_id, skill_data: SkillUpdate) -> SkillRead:
    skill_dict = skill_data.model_dump(exclude_unset=True)

    try:
        skill_to_be_updated = await get_skill_by_id(db, skill_id)

        if not skill_to_be_updated:
            raise NotFoundError('skill not found')
        
        for key, value in skill_dict.items():
            setattr(skill_to_be_updated, key, value)

        updated_skill = await update_skill(db, skill_to_be_updated)

        return updated_skill
    except Exception as e:
        raise SQLAlchemyError(detail=f'{e}')
    
async def retrieve_a_skill(db:Session, skill_id):
    try:
        skill = await get_skill_by_id(db, skill_id)
        if not skill:
            raise NotFoundError('skill not found')
        
        return skill
    except Exception as e:
        raise SQLAlchemyError(detail=f'{e}')

async def retrieve_all_skills(db:Session) -> SkillRead:
    all_skill = await get_skills(db)

    if not all_skill:
        raise NotFoundError('No skill here')
    
    return all_skill

async def delete_skill_service(db:Session, skill_id):
    try:
        deleted = await delete_skill(db, skill_id)
        return deleted
    except Exception as e:
        raise SQLAlchemyError(detail=f'{e}')
