from fastapi import Request
from typing import Any
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
async def home(request: Request) -> Any:
    return templates.TemplateResponse(
        "home.html",
        {
            "request": request,
            "sample_value": 123,
        },
    )
