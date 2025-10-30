from pydantic import BaseModel

class SocialLink(BaseModel):
    platform:str
    url:str

class Contact(BaseModel):
    phone_no: str
    whatsapp: str

class ProfileBase(BaseModel):
    full_name: str
    nickname: str
    professional_title: str
    bio:str
    email: str
    contact:Contact
    social_links: list[SocialLink]

class ProfileUpdate(ProfileBase):
    full_name: str | None = None
    nickname: str | None = None
    professional_title: str | None = None
    email: str | None = None
    contact: Contact | None = None
    bio: str | None = None
    social_links: list[SocialLink] | None = None


    class Config:
        from_attributes = True

class ProfileRead(ProfileBase):
    id: int

    class Config:
        from_attributes = True