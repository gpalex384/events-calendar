from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate
from app.utils.security import hash_password


def create_user(db: Session, payload: UserCreate) -> User:
    user = User(
        email=payload.email,
        username=payload.username,
        hashed_password=hash_password(payload.password),
        is_active=payload.is_active
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user