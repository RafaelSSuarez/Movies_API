from fastapi import APIRouter

from app.services.count_director_films import count_director_films

router = APIRouter()

@router.get(
    '/count-films-by-director',
    )
async def count_films_by_director():
    return count_director_films()