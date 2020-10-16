from fastapi import APIRouter, Depends

from app import schemas
from app.models import Animal
from app.utils.paginator import Pagination, PaginationResult

router = APIRouter()


@router.get("/animals", response_model=PaginationResult[schemas.AnimalDetail], tags=["Animal"])
async def list_animals(p: Pagination = Depends(Pagination)):
    queryset = Animal.all()
    return await p.apply(queryset, schemas.AnimalDetail)
