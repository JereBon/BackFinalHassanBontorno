from typing import Optional
from uuid import uuid4
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from repositories.client_repository import ClientRepository
from schemas.auth_schema import LoginResponse, UserOut

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class AuthenticationError(Exception):
    pass


def _verify_password(plain_password: str, stored_password: str) -> bool:
    # If stored password looks like a bcrypt hash, verify with passlib
    if stored_password and stored_password.startswith("$2"):
        try:
            return pwd_context.verify(plain_password, stored_password)
        except Exception:
            return False
    # Fallback: plain text comparison
    return plain_password == stored_password


def authenticate_user(db: Session, email: str, password: str) -> LoginResponse:
    repo = ClientRepository(db)
    client = repo.get_by_email(email)

    if client is None:
        raise AuthenticationError("Invalid credentials")

    if not _verify_password(password, getattr(client, "password", "")):
        raise AuthenticationError("Invalid credentials")

    token = str(uuid4())

    user_out = UserOut(
        id_key=client.id_key,
        email=client.email,
        name=getattr(client, "name", None),
        lastname=getattr(client, "lastname", None),
    )

    return LoginResponse(token=token, user=user_out)
