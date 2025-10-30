from sqlalchemy import String, JSON, Integer
from sqlalchemy.orm import mapped_column, Mapped
from core.db import Base
from .profile_schemas import SocialLink

class Profile(Base):
    __tablename__ = 'profile'

    id: Mapped[int] = mapped_column(
        'id',
        Integer,
        primary_key=True,
        default = 1,
        index=True
    )

    full_name: Mapped[str] = mapped_column(
        String(128),
        nullable=False,
    )

    nickname: Mapped[str] = mapped_column(
        String(128),
        nullable=False,
    )

    professional_title: Mapped[str] = mapped_column(
        String(128),
        nullable=False
    )

    bio: Mapped[str] = mapped_column(
        String(2048),
        nullable=False
    )

    email:Mapped[str] = mapped_column(
        String(256),
        nullable=False,
        unique= True
    )

    whatsapp:Mapped[str] = mapped_column(
        String(256),
        nullable=False,
        unique= True
    )

    social_links: Mapped[list[SocialLink]] = mapped_column(
        JSON,
        nullable=False
    )

    def __repr__(self):
        return f"Profile(id={self.id}, full_name='{self.full_name}')"