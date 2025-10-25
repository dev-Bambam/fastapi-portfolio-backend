from typing import List, Optional
from enum import Enum
from pydantic import BaseModel, Field

# NOTE: Import the central Base class defined in database.py
from ...database import Base 

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, Text, Enum as SQLEnum, JSON, func

# --- 1. ENUMS ---

class ProjectStatus(str, Enum):
    """Enforces valid status options for a Project."""
    COMPLETED = "Completed"
    ONGOING = "Ongoing"
    CANCELED = "Canceled"


# --- 2. SQLALCHEMY ORM MODEL ---

class ProjectModel(Base):
    """
    The SQLAlchemy ORM Model defining the 'project' table structure.
    This handles all database interactions.
    """
    __tablename__ = "project"

    # Primary Key
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    # Core fields
    title: Mapped[str] = mapped_column(String(256), nullable=False, index=True)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    
    # Status uses SQLAlchemy's Enum type
    status: Mapped[ProjectStatus] = mapped_column(
        SQLEnum(ProjectStatus), 
        default=ProjectStatus.ONGOING,
        nullable=False
    )
    
    # URLs
    github_url: Mapped[str] = mapped_column(String(512), nullable=False)
    docs_url: Mapped[Optional[str]] = mapped_column(String(512), nullable=True)
    live_url: Mapped[Optional[str]] = mapped_column(String(512), nullable=True)
    
    # tech_stack is a Python list of strings, stored as JSON in the database
    tech_stack: Mapped[List[str]] = mapped_column(
        JSON, 
        default=lambda: [], # Factory function for mutable defaults
        nullable=False
    )


# --- 3. PYDANTIC SCHEMAS FOR API INTERACTION ---

class ProjectBase(BaseModel):
    """
    Base Pydantic schema for validation and data transfer.
    Used for shared fields between creation and reading.
    """
    title: str = Field(min_length=1, max_length=256)
    description: str
    status: ProjectStatus = ProjectStatus.ONGOING
    github_url: str = Field(min_length=1)
    docs_url: Optional[str] = None
    live_url: Optional[str] = None
    tech_stack: List[str] = Field(default_factory=list)

class Project(ProjectBase):
    """
    The full Project schema used for reading data out of the API.
    It includes the database-generated ID.
    """
    id: int

    class Config:
        # Essential for reading data from the SQLAlchemy ORM Model
        from_attributes = True

class ProjectCreate(ProjectBase):
    """Schema for creating a new Project."""
    pass # Inherits all necessary fields

class ProjectUpdate(BaseModel):
    """
    Schema for updating an existing Project (all fields optional).
    Fields are Optional because we only send what needs changing.
    """
    title: Optional[str] = Field(None, min_length=1, max_length=256)
    description: Optional[str] = None
    status: Optional[ProjectStatus] = None
    github_url: Optional[str] = Field(None, min_length=1)
    docs_url: Optional[str] = None
    live_url: Optional[str] = None
    tech_stack: Optional[List[str]] = None
