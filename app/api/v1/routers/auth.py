from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app import crud, schemas
from app.core import security
from app.core.config import settings
from app.api import deps

router = APIRouter()


@router.post("/token", response_model=schemas.Token)
def login_for_access_token(
        db: Session = Depends(
            deps.get_db),
        form_data: OAuth2PasswordRequestForm = Depends()):
    user = crud.user.authenticate(
        db,
        username=form_data.username,
        password=form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/register", response_model=schemas.User)
def register_user(
    user: schemas.UserCreate,
    db: Session = Depends(
        deps.get_db)):
    db_user = crud.user.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(
            status_code=400,
            detail="Username already registered",
        )
    return crud.user.create_user(db=db, user=user)
