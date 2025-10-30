from .project_repo import (
    create_project, update_project,
    delete_project, get_project_by_id,
    get_projects
)
from src.utils.error.errors import (
    NotFoundError
)
from .project_schemas import (
    ProjectCreate, ProjectUpdate,
    Project
)

async def create_project_service(db, project_data:ProjectCreate)-> Project:
    project_dict = project_data.model_dump()

    new_project = await create_project(db, project_dict)
    return new_project
    
    
async def update_project_service(db, id, project_data:ProjectUpdate) -> Project:
    project_dict = project_data.model_dump(exclude_unset=True)

    project_to_update = await get_project_by_id(db, id)
    if not project_to_update:
        raise NotFoundError('Project not found')
    
    for key, value in project_dict.items():
        setattr(project_to_update, key, value)

    updated_project = await update_project(db, project_to_update)
    return updated_project
    
    
async def fetch_a_project(db, id)->Project | None:
    
        project = await get_project_by_id(db, id)
        if not project:
            raise NotFoundError('project not found')
        return project
    
    
async def fetch_all_project(db) -> list[Project] | None:
   
        projects = await get_projects(db)
        if len(projects) == 0:
            raise NotFoundError('No projects yet')
        
        return projects
    
    
async def delete_project_service(db, id) ->bool:
    
        project_to_delete = await get_project_by_id(db, id)
        if not project_to_delete:
            raise NotFoundError('project not found')
        success = await delete_project(db, project=project_to_delete)

        
        return {"success":success}
    
