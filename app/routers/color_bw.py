from fastapi import APIRouter

from app.services.count_color_bw import count_color_bw

router = APIRouter()

@router.get(
    '/count-color-black-and-white',
    )
async def count_color_black_and_white_movies():
    return count_color_bw()