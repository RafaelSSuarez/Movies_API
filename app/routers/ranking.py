from fastapi import APIRouter

from app.services.actors_ranking import ranking


router = APIRouter()
@router.get(
    '/actors_ranking/{limit}'
)
async def actors_ranking(limit:int):
    return ranking(limit) 