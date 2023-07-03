from typing import Optional

from fastapi import APIRouter
from pydantic import BaseModel

routes_eg3 = APIRouter(prefix="/example1")


my_data = {
    "street_number": 1,
    "street_name": "Park",
    "street_suffix": "Rd",
}

class MyModel(BaseModel):
    unit_number: Optional[str]
    street_number: int
    street_name: str
    street_suffix: str

@routes_eg3.get("/")
async def basic_data(pk: Optional[int] = None):
    return MyModel(**my_data)
