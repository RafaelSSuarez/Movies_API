from fastapi import FastAPI

from .core.settings import settings
from .routers.routers import add_routers

app = FastAPI(
    title=settings.WEB_APP_TITLE,
    description=settings.WEB_APP_DESCRIPTION,
    version=settings.WEB_APP_VERSION,
)

add_routers(app)