from typing import TYPE_CHECKING

from sqlalchemy import func, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class File(Base):
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    url = Column(String(2000))
    name = Column(String(255), index=True)
    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User", back_populates="items")
    time_updated = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
    time_created = Column(DateTime(timezone=True), server_default=func.now())
