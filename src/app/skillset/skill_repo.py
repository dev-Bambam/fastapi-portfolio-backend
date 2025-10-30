from sqlalchemy.ext.asyncio import AsyncSession
from .skill_model import Skill
from sqlalchemy import select, delete
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

async def create_skill(db:AsyncSession, skill_data:dict):
    new_skill = Skill(**skill_data)
    try:
        db.add(new_skill)
        await db.commit()
        await db.refresh(new_skill)
        return new_skill
    except SQLAlchemyError as e:
        await db.rollback()
        raise e
    except IntegrityError as e:
        await db.rollback()
        raise e
    
async def update_skill(db:AsyncSession, skill_data:dict):
    try:
        db.add(skill_data)
        await db.commit()
        await db.refresh(skill_data)
        return skill_data
    except SQLAlchemyError as e:
        await db.rollback()
        raise e
    except IntegrityError as e:
        await db.rollback()
        raise e
    
async def get_skills(db:AsyncSession):
    stmt = select(Skill).order_by(Skill.created_at.desc())
    result = await db.scalars(stmt)
    skills = result.all()
    return skills

async def get_skill_by_id(db:AsyncSession, id):
    stmt = select(Skill).where(Skill.id == id)
    skill = await db.scalar(stmt)
    
    return skill

async def delete_skill(db:AsyncSession, id) -> bool:
    stmt = delete(Skill).where(Skill.id == id)
    try:
        result = await db.execute(stmt)
        await db.commit()
        deleted_count = result.rowcount if result else 0

        return deleted_count > 0
    except SQLAlchemyError as e:
        await db.rollback()
        raise e