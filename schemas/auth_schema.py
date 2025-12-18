from pydantic import Field
from schemas.base_schema import BaseSchema
from typing import Optional


class LoginRequest(BaseSchema):
    email: str = Field(..., example="user@example.com")
    password: str = Field(..., example="secret123")


class UserOut(BaseSchema):
    email: str
    name: Optional[str] = None
    lastname: Optional[str] = None


class LoginResponse(BaseSchema):
    token: str
    user: UserOut
