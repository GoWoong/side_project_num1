from fastapi import APIRouter
from fastapi import Request, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from db.repository.jobs import list_jobs, retreive_job
from db.session import get_db
from typing import Optional
from db.repository.jobs import search_job

templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)


@router.get("/")
async def home(request: Request, db: Session = Depends(get_db), msg: str = None):  # new
    jobs = list_jobs(db=db)
    return templates.TemplateResponse(
        "general_pages/homepage.html",
        {"request": request, "jobs": jobs, "msg": msg},  # new
    )


@router.get("/details/{id}")  # new
def job_detail(id: int, request: Request, db: Session = Depends(get_db)):
    job = retreive_job(id=id, db=db)
    return templates.TemplateResponse(
        "jobs/detail.html", {"request": request, "job": job}
    )


@router.get("/delete-job/")
def show_jobs_to_delete(request: Request, db: Session = Depends(get_db)):
    jobs = list_jobs(db=db)
    return templates.TemplateResponse(
        "jobs/show_jobs_to_delete.html", {"request": request, "jobs": jobs}
    )


@router.get("/search/")
def search(
    request: Request, db: Session = Depends(get_db), query: Optional[str] = None
):
    jobs = search_job(query, db=db)
    return templates.TemplateResponse(
        "general_pages/homepage.html", {"request": request, "jobs": jobs}
    )
