from fastapi import APIRouter, Depends
from .project_service import (
    create_project_service, update_project_service,
    delete_project_service, fetch_a_project,
    fetch_all_project
)
from core.db import get_db
from .project_schemas import (
    Project, ProjectCreate, ProjectUpdate
)
from uuid import UUID

router = APIRouter(prefix='/projects',)

@router.post('/', response_model=Project)
async def create_project(project_data:ProjectCreate, db=Depends(get_db)):
    return await create_project_service(db, project_data)

@router.put('/{id}', response_model=Project)
async def update_project(id:UUID, project_data:ProjectUpdate, db=Depends(get_db)):
    return await update_project_service(db, id, project_data)

@router.get('/', response_model=list[Project])
async def read_all_project(db=Depends(get_db)):
    return await fetch_all_project(db)

@router.get('/{id}', response_model=Project)
async def read_a_project(id:UUID, db=Depends(get_db)):
    return await fetch_a_project(db, id)

@router.delete('/{id}', response_model=bool)
async def delete_project(id:UUID, db=Depends(get_db)):
    return await delete_project_service(db, id)