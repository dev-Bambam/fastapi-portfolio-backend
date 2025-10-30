from .project_model import Project
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

async def create_project(db:AsyncSession, project_data:dict) -> Project:
    new_project = Project(**project_data)

    try:
        db.add(new_project)
        await db.commit()
        await db.refresh(new_project)

        return new_project
    except IntegrityError as e:
        await db.rollback()
        return e
    except SQLAlchemyError as e:
        await db.rollback()
        return e
    
async def get_project_by_id(db:AsyncSession, id) -> Project | None :
    stmt = select(Project).where(Project.id == id).filter(Project.is_deleted.is_(False))
    project = db.scalar(stmt)

    return project

async def get_projects(db:AsyncSession) -> list[Project] | None:
    stmt = select(Project).order_by(Project.created_at.desc()).where(Project.is_deleted.is_(False))
    projects = await db.scalars(stmt).all()

    return projects

async def update_project(db:AsyncSession, project_data:dict) -> Project:
    try:
        db.add(project_data)
        await db.commit()
        await db.refresh(project_data)

        return project_data
    except SQLAlchemyError as e:
        await db.rollback()
        return e
    except IntegrityError as e:
        await db.rollback()
        return e
    
async def delete_project(db:AsyncSession, project:Project) -> bool:
    Project.is_deleted = True
    return True
