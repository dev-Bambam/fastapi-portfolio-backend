from fastapi import APIRouter, Depends
from uuid import UUID

from src.app.profile.profile_service import get_profile_service, ProfileBase
from src.app.project.project_service import (
    fetch_all_project,
    fetch_a_project, Project
)
from src.app.skillset.skill_service import(
    retrieve_a_skill,
    retrieve_all_skills, SkillRead
)
from core.db import get_db

router = APIRouter(prefix='/clients', tags=['Client'])

@router.get('/profiles', response_model=ProfileBase)
async def get_profile(db=Depends(get_db)):
    return await get_profile_service(db)

@router.get('/skills', response_model=SkillRead)
async def get_all_skills(db=Depends(get_db)):
    return await retrieve_all_skills(db)

@router.get('/skills/{id}', response_model=SkillRead)
async def get_a_skill(id:UUID, db=Depends(get_db)):
    print(f'db from route:{db}')
    return await retrieve_a_skill(db, id)

@router.get('/projects', response_model=Project)
async def get_all_project(db=Depends(get_db)):
    return await fetch_all_project(db)

@router.get('/projects/{id}', response_model=Project)
async def get_a_project(id:UUID, db=Depends(get_db)):
    return await fetch_a_project(db, id)