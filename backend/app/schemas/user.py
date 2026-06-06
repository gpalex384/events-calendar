from typing import Optional
from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserBase(BaseModel):
    email: EmailStr
    username: str = Field(..., max_length=150, min_length=5)
    is_active: bool = True


class UserCreate(UserBase):
    password: str = Field(..., min_length=8, max_length=72)


class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    username: Optional[str] = Field(None, max_length=150, min_length=5)
    password: Optional[str] = None
    is_active: bool = True


class UserOut(UserBase):
    id: int
    created: datetime
    model_config = ConfigDict(from_attributes=True)
