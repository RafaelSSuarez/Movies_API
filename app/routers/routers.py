from fastapi import FastAPI

from .color_bw import router as color_bw_router
from .film_director import router as film_director_router
from .films_sort_by_column import router as less_critiziced_router

def add_routers(app: FastAPI) -> None:
    """
    """
    app.include_router(color_bw_router)
    app.include_router(film_director_router)
    app.include_router(less_critiziced_router)
