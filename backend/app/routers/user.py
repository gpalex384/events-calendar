# app/routers/user.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies.dependencies import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserOut
from app.services.userservice import create_user

router = APIRouter(prefix="/users", tags=["users"])


@router.post("", response_model=UserOut)
def register_user(
    payload: UserCreate,
    db: Session = Depends(get_db)
):
    return create_user(db, payload)