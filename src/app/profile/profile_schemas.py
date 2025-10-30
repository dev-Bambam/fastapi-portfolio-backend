from pydantic import BaseModel

class SocialLink(BaseModel):
    platform:str
    url:str

class ProfileBase(BaseModel):
    full_name: str
    nickname: str
    professional_title: str
    bio:str
    email: str
    whatsapp:str
    social_links: list[SocialLink]

class ProfileUpdate(ProfileBase):
    full_name: str | None = None
    nickname: str
    professional_title: str | None = None
    email: str | None = None
    whatsapp: str | None = None
    bio: str | None = None
    social_links: list[SocialLink]


    class Config:
        from_attributes = True

class ProfileRead(ProfileBase):
    id: int

    class Config:
        from_attributes = True