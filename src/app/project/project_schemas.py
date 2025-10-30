from pydantic import BaseModel, Field
from .project_model import ProjectStatus
from uuid import UUID


class ProjectBase(BaseModel):
    """
    Base Pydantic schema for validation and data transfer.
    Used for shared fields between creation and reading.
    """
    title: str = Field(min_length=1, max_length=256)
    description: str
    status: ProjectStatus = ProjectStatus.ONGOING
    github_url: str = Field(min_length=1)
    docs_url: str 
    live_url: str | None = None
    tech_stack: list[str] = Field(default_factory=list)

class Project(ProjectBase):
    """
    The full Project schema used for reading data out of the API.
    It includes the database-generated ID.
    """
    id: UUID

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
    title: str | None = Field(None, min_length=1, max_length=256)
    description: str | None = None
    status: ProjectStatus | None = None
    github_url: str | None = Field(None, min_length=1)
    docs_url: str | None = None
    live_url: str | None = None
    tech_stack: list[str] | None = None

class DeleteRes(BaseModel):
    success:bool
