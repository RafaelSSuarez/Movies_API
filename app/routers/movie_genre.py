from fastapi import APIRouter

from app.services.movie_genre import movie_genre_each_year


router = APIRouter()
@router.get(
    '/movie_genre_each_year/{gross_income}'
)
async def movie_genre_endpoint(gross_income:str):
    return movie_genre_each_year(gross_income) 