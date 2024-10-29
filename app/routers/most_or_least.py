from fastapi import APIRouter

from app.services.year_with_most_or_least_films import year_most_or_least_films
from app.schemas.params import most_or_least


router = APIRouter()
@router.get(
    '/year_with_most_or_least_movies/{desired_year}'
)
async def most_or_least_movies(
        desired_year:most_or_least
):
    return year_most_or_least_films(desired_year.value)


