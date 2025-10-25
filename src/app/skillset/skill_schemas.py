from pydantic import BaseModel, Field, UUID4

class SkillBase(BaseModel):
    name: str = Field(
        ...,
        min_length=2,
        max_length=128,
        description='The name of the skill'
    )

    level: int = Field(
        ...,
        ge=1,
        le=5,
        description='Proficiency level (1=Beginner, 5=Exper)'
    )

    category: str | None = Field(
        None,
        max_length=64,
        description='Optional grouping category'
    )

class SkillCreate(SkillBase):
    pass

class SkillUpdate(BaseModel):
    name: str | None =Field(None, min_length=2, max_length=128)

    level: int | None = Field(None, ge=1, le=5)
    category: str|None = Field(None, max_length=64)

class SkillRead(SkillBase):
    id: UUID4

    class Config:
        from_attributes = True