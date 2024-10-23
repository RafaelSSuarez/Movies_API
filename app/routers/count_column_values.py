from fastapi import APIRouter

from app.schemas.columns import RequiredUniqueValuesColumns
from app.services.count_unique_values import count_unique_values


router = APIRouter()

@router.get(
    '/count-column-values/{column_name}',
    )
async def count_unique_values_in_column(
    column_name:RequiredUniqueValuesColumns
):
    return count_unique_values(column_name.value)