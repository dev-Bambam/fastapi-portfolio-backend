from sqlalchemy.orm import Session
from .skill_model import Skill
from sqlalchemy import select, delete
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

def create_skill(db:Session, skill_data:dict):
    new_skill = Skill(**skill_data)
    try:
        db.add(new_skill)
        db.commit()
        db.refresh(new_skill)
        return new_skill
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    except IntegrityError as e:
        db.rollback()
        raise e
    
def update_skill(db:Session, skill_data:dict):
    try:
        db.add(skill_data)
        db.commit()
        db.refresh(skill_data)
        return skill_data
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    except IntegrityError as e:
        db.rollback()
        raise e
    
def get_skills(db:Session):
    stmt = select(Skill)
    skills = db.scalars(stmt).all()
    
    return skills

def get_skill_by_id(db:Session, id):
    stmt = select(Skill).where(Skill.id == id)
    skill = db.scalar(stmt)

    return skill

def delete_skill(db:Session, id):
    stmt = delete(Skill).where(Skill.id == id)
    try:
        result = db.execute(stmt)
        db.commit()
        deleted_count = result.rowcount if result else 0

        return deleted_count > 0
    except SQLAlchemyError as e:
        db.rollback()
        raise e