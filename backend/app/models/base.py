from datetime import datetime, timezone
from sqlalchemy import Column, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BaseModel(Base):
    """Base model with audit fields for all models to inherit from"""
    __abstract__ = True

    created = Column(DateTime, default=datetime.now(timezone.utc), nullable=False)
    updated = Column(DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc), nullable=False)
    active = Column(Boolean, default=True, nullable=False)
