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
        raise e
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    
async def 