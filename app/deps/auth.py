from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jwt.exceptions import InvalidTokenError, PyJWTError
from pydantic import ValidationError
from app.core.security import verify_token, verify_password, TokenData
from app.models import User
from app.core.database import get_db
from app.schemas import UserRole

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth/token")


def get_db_user(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def authenticate_user(db: Session, email: str, password: str):
    user = get_db_user(db, email)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def get_current_active_user(
        token: str = Depends(oauth2_scheme),
        db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = verify_token(token)
        if payload is None:
            raise credentials_exception
        email: str = payload.email
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except (PyJWTError, InvalidTokenError, ValidationError):
        raise credentials_exception
    user = get_db_user(db, token_data.email)
    if user is None:
        raise credentials_exception
    return user


def admin_or_manager(user: User = Depends(get_current_active_user)):
    if user.role not in {UserRole.admin, UserRole.manager}:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions",
        )
    return user


def current_user_or_admin(
        user_id: int,
        current_user: User = Depends(get_current_active_user)):
    if current_user.id != user_id and current_user.role != UserRole.admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions",
        )
    return current_user
