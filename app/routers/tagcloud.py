from fastapi import APIRouter

from app.services.tag_cloud import tag_cloud


router = APIRouter()
@router.get(
    '/tagcloud'
)
async def something():
    return tag_cloud()