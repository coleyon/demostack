from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Task])
def read_tasks(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve tasks.
    """
    if crud.user.is_superuser(current_user):
        tasks = crud.task.get_multi(db, skip=skip, limit=limit)
    else:
        tasks = crud.tasks.get_multi_by_owner(
            db=db, owner_id=current_user.id, skip=skip, limit=limit
        )
    return tasks


@router.post("/", response_model=schemas.Task)
def create_task(
    *,
    db: Session = Depends(deps.get_db),
    task_in: schemas.TaskCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new task.
    """
    task = crud.task.create_with_owner(db=db, obj_in=task_in, owner_id=current_user.id)
    return task


@router.put("/{id}", response_model=schemas.Task)
def update_task(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    task_in: schemas.TaskUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update an task.
    """
    task = crud.task.get(db=db, id=id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    if not crud.user.is_superuser(current_user) and (task.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    task = crud.task.update(db=db, db_obj=task, obj_in=task_in)
    return task


@router.get("/{id}", response_model=schemas.Task)
def read_task(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get Task by ID.
    """
    task = crud.task.get(db=db, id=id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    if not crud.user.is_superuser(current_user) and (task.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return task


@router.delete("/{id}", response_model=schemas.Task)
def delete_task(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete an task.
    """
    task = crud.task.get(db=db, id=id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    if not crud.user.is_superuser(current_user) and (task.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    task = crud.task.remove(db=db, id=id)
    return task
