import pydantic
from tortoise.contrib.pydantic import pydantic_model_creator

from app.models import Animal


class Schema(pydantic.BaseModel):
    class Config:
        orm_mode = True
        anystr_strip_whitespace = True


AnimalDetail = pydantic_model_creator(Animal)
