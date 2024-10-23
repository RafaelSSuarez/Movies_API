from fastapi import FastAPI

from .count_column_values import router as count_router
from .films_sort_by_column import router as sort_router
def add_routers(app: FastAPI) -> None:
    """
    Includes all routers to the API
    """
    app.include_router(count_router)
    app.include_router(sort_router)
