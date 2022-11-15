from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from core.config import settings
from apis.general_pages.route_homepage import general_pates_router


def include_router(app):
    app.include_router(general_pates_router)


def configure_static(app):
    app.mount("/static", StaticFiles(directory="static"), name="static")


# fastapi
def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    include_router(app)
    configure_static(app)
    return app


app = start_application()

# @app.get("/")
# async def read_root():
#     return {"Hello": "World"}
