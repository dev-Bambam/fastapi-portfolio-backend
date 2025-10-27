from .project_model import Project
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

async def create_project(db:Session, project_data:dict) -> Project:
    new_project = Project(**project_data)

    try:
        db.add(new_project)
        db.commit()
        db.refresh(new_project)

        return new_project
    except IntegrityError as e:
        db.rollback()
        return e
    except SQLAlchemyError as e:
        db.rollback()
        return e
    
async def get_project_by_id(db:Session, id) -> Project | None :
    stmt = select(Project).where(Project.id == id).filter_by(not Project.is_deleted)
    project = db.scalars(stmt)

    return project

async def get_projects(db:Session) -> list[Project] | None:
    stmt = select(Project).order_by(Project.created_at.desc()).where(Project.is_deleted.is_(False))
    projects = db.scalars(stmt).all()

    return projects

async def update_project(db:Session, project_data:dict) -> Project:
    try:
        db.add(project_data)
        db.commit()
        db.refresh(project_data)

        return project_data
    except SQLAlchemyError as e:
        db.rollback()
        return e
    except IntegrityError as e:
        db.rollback()
        return e
    
async def delete_project(db:Session, project:Project) -> bool:
    Project.is_deleted = True
    return True
