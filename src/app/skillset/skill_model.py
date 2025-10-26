from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String, Integer, UUID, DateTime

from core.db import Base
from uuid import uuid4
from datetime import datetime

class Skill(Base):
    __tablename__ = 'skill'

    id:Mapped[uuid4] = mapped_column(
        UUID,
        primary_key=True,
        index=True,
        default=uuid4
    )

    name:Mapped[str] = mapped_column(
        String(128),
        nullable=False,
        unique=True
    )

    level:Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    category: Mapped[str | None] = mapped_column(
        String(64),
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default= datetime.now()
    )
    
    def __repr__(self):
        return f"Skill(id={self.id}, name={self.name}, level={self.level})"