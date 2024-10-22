from fastapi import APIRouter

from app.services.films_sorted_by_column import sort_by_column
from app.schemas.columns import RequiredIntColumns


router = APIRouter()

@router.get(
    '/sort-movies-by-column/{colum_name}'
    )
async def sort_movies_by_colum(
    colum_name:RequiredIntColumns,
    limit:int, 
    highest_first:bool = False
):
    return sort_by_column(colum_name.value,limit,highest_first)