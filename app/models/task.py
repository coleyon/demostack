from typing import TYPE_CHECKING

from sqlalchemy import func, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from app.schemas.task import TaskCreate

if TYPE_CHECKING:
    from .user import User  # noqa: F401


class Task(Base):
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(255), index=True)
    description = Column(String(255), server_default="")
    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User", back_populates="items")
    time_updated = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
    time_created = Column(DateTime(timezone=True), server_default=func.now())
