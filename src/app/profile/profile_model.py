from sqlalchemy import Column, String, JSON
from core.db import Base
from .profile_schemas import SocialLink

class Profile(Base):
    __tablename__ = 'profile'

    id: int | None = Column(
        'id',
        String,
        primary_key=True,
        default = 1,
        index=True
    )

    full_name: str = Column(
        String(128),
        nullable=False,
    )

    nickname: str = Column(
        String(128),
        nullable=False,
    )

    professional_title: str = Column(
        String(128),
        nullable=False
    )

    bio: str = Column(
        String(2048),
        nullable=False
    )

    email:str = Column(
        String(256),
        nullable=False,
        unique= True
    )

    social_links: list[SocialLink] = Column(
        JSON,
        nullable=False
    )

    def __repr__(self):
        return f"Profile(id={self.id}, full_name='{self.full_name}')"