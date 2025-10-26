from fastapi import APIRouter, Depends
from core.db import get_db

from .skill_service import (
    create_skill_service, delete_skill_service,
    update_skill_service, retrieve_a_skill,
    retrieve_all_skills
)
from .skill_schemas import (
    SkillRead, SkillCreate,
    SkillUpdate
)

router = APIRouter(
    prefix='/skills'
)

@router.get('/', response_model=SkillRead)
async def fetch_all_skill(db=Depends(get_db)):
    return await retrieve_all_skills(db)

@router.get('/{skill_id}', response_model=SkillRead)
async def fetch_a_skill(skill_id, db=Depends(get_db)):
    return await retrieve_a_skill(db, skill_id)

@router.post('/', response_model=SkillRead)
async def create_skill(skill_data:SkillCreate, db=Depends(get_db)):
    return await create_skill_service(db, skill_data)

@router.put('/{skill_id}', response_model=SkillRead)
async def update_skill(skill_id, skill_data:SkillUpdate, db=Depends(get_db)):
    return await update_skill_service(skill_id, skill_data, db)

@router.delete('/{skill_id}', response_model=bool)
async def delete_skill(skill_id, db=Depends(get_db)):
    return await delete_skill_service(skill_id, db)