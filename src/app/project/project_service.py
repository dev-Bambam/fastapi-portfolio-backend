from .project_repo import (
    create_project, update_project,
    delete_project, get_project_by_id,
    get_projects
)
from src.utils.error.errors import (
    NotFoundError, SQLAlchemyError
)
from .project_schemas import (
    ProjectCreate, ProjectUpdate,
    Project
)

async def create_project_service(db, project_data:ProjectCreate)-> Project:
    project_dict = project_data.model_dump()

    try:
        new_project = await create_project(db, project_dict)
        return new_project
    except Exception as e:
        raise SQLAlchemyError(detail=f'{e}')
    
async def update_project_service(db, id, project_data:ProjectUpdate) -> Project:
    project_dict = project_data.model_dump(exclude_unset=True)

    project_to_update = await get_project_by_id(db, id)
    if not project_to_update:
        raise NotFoundError('Project not found')
    
    for key, value in project_dict.items():
        setattr(project_to_update, key, value)
    
    try:
        updated_project = await update_project(db, project_to_update)
        return updated_project
    except Exception as e:
        raise SQLAlchemyError(detail=f'{e}')
    
async def fetch_a_project(db, id)->Project | None:
    try:
        project = await get_project_by_id(db, id)
        if not project:
            raise NotFoundError('project not found')
        return project
    except Exception as e:
        raise SQLAlchemyError(detail=f'{e}')
    
async def fetch_all_project(db) -> list[Project] | None:
    try:
        projects = await get_projects(db)
        if not projects:
            raise NotFoundError('No projects yet')
        return projects
    except Exception as e:
        raise SQLAlchemyError(detail=f'{e}')
    
async def delete_project_service(db, id) ->bool:
    try:
        project_to_delete = await get_project_by_id(db, id)
        if not project_to_delete:
            raise NotFoundError('project not found')
        is_deleted = await delete_project(project_to_delete)

        return is_deleted
    except Exception as e:
        raise SQLAlchemyError(f'{e}')
