from typing import TYPE_CHECKING

from sqlalchemy import func, Boolean, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from app.db.base_class import Base

if TYPE_CHECKING:
    from .item import Item  # noqa: F401
    from .task import Task  # noqa: F401
    from .file import File  # noqa: F401
    from .applog import AppLog  # noqa: F401


class User(Base):
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    full_name = Column(String(255), index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    items = relationship("Item", back_populates="owner")
    time_updated = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
    time_created = Column(DateTime(timezone=True), server_default=func.now())
