from typing import Optional
from pydantic import BaseModel, AnyUrl


# Shared properties
class FileBase(BaseModel):
    url: Optional[str] = None
    name: Optional[str] = None


# Properties to receive on File creation
class FileCreate(FileBase):
    url: str


# Properties to receive on File update
class FileUpdate(FileBase):
    pass


# Properties shared by models stored in DB
class FileInDBBase(FileBase):
    id: int
    name: str
    url: AnyUrl

    class Config:
        orm_mode = True


# Properties to return to client
class File(FileInDBBase):
    pass


# Properties properties stored in DB
class FileInDB(FileInDBBase):
    pass
