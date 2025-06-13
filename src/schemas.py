from datetime import datetime
from typing import List, Optional
from  datetime import date
from pydantic import BaseModel, EmailStr, Field


class ContactBase(BaseModel):
    name: str
    surname: str
    email: EmailStr
    phone: str
    birthday: date
    info: Optional[str] = None


class ContactCreate(ContactBase):
    pass


class ContactUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=15)
    surname: Optional[str] = Field(None, max_length=15)
    email: Optional[EmailStr] = None
    phone: Optional[str] = Field(None, max_length=15)
    birthday: Optional[date] = None
    info: Optional[str] = None


class ContactResponse(ContactBase):
    id: int

    class Config:
        from_attributes = True
