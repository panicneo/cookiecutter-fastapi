from fastapi import APIRouter
from app.controllers import animals

router = APIRouter()
router.include(animals.router)
