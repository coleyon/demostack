from typing import Optional
from pydantic import BaseModel


# Shared properties
class TaskBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


# Properties to receive on Task creation
class TaskCreate(TaskBase):
    title: str


# Properties to receive on Task update
class TaskUpdate(TaskBase):
    pass


# Properties shared by models stored in DB
class TaskInDBBase(TaskBase):
    id: int
    title: str
    description: str

    class Config:
        orm_mode = True


# Properties to return to client
class Task(TaskInDBBase):
    pass


# Properties properties stored in DB
class TaskInDB(TaskInDBBase):
    pass
