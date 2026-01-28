from typing import Optional
from pydantic import BaseModel, EmailStr

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id_key: int # Added ID
    email: EmailStr
    name: Optional[str] = None
    lastname: Optional[str] = None

class LoginResponse(BaseModel):
    token: str
    user: UserOut
