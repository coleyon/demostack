from fastapi import Request
from typing import Any

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from asyncio import sleep
from datetime import datetime as dt

from fastapi import APIRouter

# from fastapi import Depends
# from sqlalchemy.orm import Session
# from app.api import deps
# from app import crud, models, schemas


router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
async def home(request: Request) -> Any:
    receive = dt.utcnow()
    await sleep(5)
    resp = (dt.utcnow() - receive) * 1000
    return templates.TemplateResponse(
        "home.html",
        {
            "request": request,
            "sample_value": f"home {resp.total_seconds()}",
        },
    )


# @router.get("/item/", response_class=HTMLResponse)
# async def item(request: Request, db: Session = Depends(deps.get_db)) -> Any:
#     item = crud.item.create_with_owner(
#         db=db, obj_in=item_in, owner_id=current_user.id
#     )
#     receive = dt.utcnow()
#     resp = (dt.utcnow() - receive) * 1000
#     return templates.TemplateResponse(
#         "home.html",
#         {
#             "request": request,
#             "sample_value": f"item {resp.total_seconds()}",
#         },
#     )
