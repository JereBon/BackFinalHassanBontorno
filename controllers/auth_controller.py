from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from config.database import get_db
from schemas.auth_schema import LoginRequest, LoginResponse
from services.auth_service import authenticate_user, AuthenticationError

router = APIRouter(tags=["Auth"])


@router.post("/login", response_model=LoginResponse, status_code=status.HTTP_200_OK)
async def login(payload: LoginRequest, db: Session = Depends(get_db)):
    """Authenticate user and return token with user info."""
    try:
        result = authenticate_user(db, payload.email, payload.password)
        return result
    except AuthenticationError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
