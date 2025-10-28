from enum import Enum
from datetime import datetime
from uuid import uuid4, UUID

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Text, Enum as SQLEnum, JSON, UUID as SQL_UUID, DateTime, Boolean


from core.db import Base

# --- 1. ENUMS ---

class ProjectStatus(str, Enum):
    """Enforces valid status options for a Project."""
    COMPLETED = "Completed"
    ONGOING = "Ongoing"
    CANCELED = "Canceled"


# --- 2. SQLALCHEMY ORM MODEL ---

class Project(Base):
    """
    The SQLAlchemy ORM Model defining the 'project' table structure.
    This handles all database interactions.
    """
    __tablename__ = "project"

    # Primary Key
    id: Mapped[UUID] = mapped_column(SQL_UUID, primary_key=True, default=uuid4)

    # Core fields
    title: Mapped[str] = mapped_column(String(256), nullable=False, index=True, unique=True)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    
    # Status uses SQLAlchemy's Enum type
    status: Mapped[ProjectStatus | None ] = mapped_column(
        SQLEnum(ProjectStatus), 
        default=ProjectStatus.ONGOING,
        nullable=False
    )
    
    # URLs
    github_url: Mapped[str] = mapped_column(String(512), nullable=False)
    docs_url: Mapped[str]  = mapped_column(String(512), nullable=False)
    live_url: Mapped[str | None]  = mapped_column(String(512), nullable=True)
    
    # tech_stack is a Python list of strings, stored as JSON in the database
    tech_stack: Mapped[list[str]] = mapped_column(
        JSON, 
        default=lambda: [], # Factory function for mutable defaults
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default= datetime.now()
    )

    is_deleted: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )
    def __repr__(self):
        return f"Skill(id={self.id}, name={self.title}"
