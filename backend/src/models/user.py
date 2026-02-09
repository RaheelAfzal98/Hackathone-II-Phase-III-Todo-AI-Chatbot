from sqlmodel import SQLModel, Field, Column, DateTime
from typing import Optional
from datetime import datetime
import uuid
from pydantic import BaseModel, EmailStr


def get_current_time():
    return datetime.utcnow()


def get_uuid():
    return str(uuid.uuid4())


class UserBase(SQLModel):
    email: EmailStr = Field(unique=True, nullable=False)
    name: str = Field(nullable=False, min_length=1, max_length=100)


class User(UserBase, table=True):
    __tablename__ = "users"  # Use 'users' instead of 'user' to avoid PostgreSQL reserved keyword
    id: str = Field(default_factory=get_uuid, primary_key=True)
    hashed_password: str = Field(nullable=False)
    created_at: datetime = Field(default_factory=get_current_time)
    updated_at: datetime = Field(default_factory=get_current_time)


class UserCreate(UserBase):
    password: str = Field(min_length=6, max_length=100)
    confirm_password: str = Field(min_length=6, max_length=100)

    def __init__(self, **data):
        super().__init__(**data)
        # Validate passwords match
        if data.get('password') != data.get('confirm_password'):
            raise ValueError("Passwords do not match")


class UserUpdate(SQLModel):
    name: Optional[str] = Field(default=None, min_length=1, max_length=100)
    email: Optional[EmailStr] = Field(default=None)


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(UserBase):
    id: str
    created_at: datetime
    token: str  # JWT token for authentication


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    user_id: str