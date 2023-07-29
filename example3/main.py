from typing import Literal, Optional

from fastapi import APIRouter
from pydantic import BaseModel

routes_eg3 = APIRouter(prefix="/example3")

StateTerritory = Literal["ACT", "NSW", "NT", "OT", "QLD", "SA", "TAS", "VIC", "WA"]


class FeatureProperty(BaseModel):
    address_id: str
    street_number: str
    street_name: str
    locality: str
    postcode: str
    state: Literal[StateTerritory]


async def get_properties(address_id: str):
    return {
        "address_id": address_id,
        "street_number": "101",
        "street_name": "North Terrace",
        "locality": "Adelaide",
        "postcode": "5000",
        "state": "ACT"
    }


@routes_eg3.get("/feature/properties")
async def feature_properties(address_id: str = "GA1") -> FeatureProperty:
    properties_kwargs: dict = await get_properties(address_id)
    return FeatureProperty(**properties_kwargs)
