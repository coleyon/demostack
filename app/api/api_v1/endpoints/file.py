from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.File])
def read_files(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve files.
    """
    if crud.user.is_superuser(current_user):
        files = crud.file.get_multi(db, skip=skip, limit=limit)
    else:
        files = crud.files.get_multi_by_owner(
            db=db, owner_id=current_user.id, skip=skip, limit=limit
        )
    return files


@router.post("/", response_model=schemas.File)
def create_file(
    *,
    db: Session = Depends(deps.get_db),
    file_in: schemas.FileCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new file.
    """
    file = crud.file.create_with_owner(db=db, obj_in=file_in, owner_id=current_user.id)
    return file


@router.put("/{id}", response_model=schemas.File)
def update_file(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    file_in: schemas.FileUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update an file.
    """
    file = crud.file.get(db=db, id=id)
    if not file:
        raise HTTPException(status_code=404, detail="File not found")
    if not crud.user.is_superuser(current_user) and (file.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    file = crud.file.update(db=db, db_obj=file, obj_in=file_in)
    return file


@router.get("/{id}", response_model=schemas.File)
def read_file(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get File by ID.
    """
    file = crud.file.get(db=db, id=id)
    if not file:
        raise HTTPException(status_code=404, detail="File not found")
    if not crud.user.is_superuser(current_user) and (file.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return file


@router.delete("/{id}", response_model=schemas.File)
def delete_file(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete an file.
    """
    file = crud.file.get(db=db, id=id)
    if not file:
        raise HTTPException(status_code=404, detail="File not found")
    if not crud.user.is_superuser(current_user) and (file.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    file = crud.file.remove(db=db, id=id)
    return file
