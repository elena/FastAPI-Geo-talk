"""
Example:

Basic parameter input.
"""
from typing import Dict, List
from fastapi import APIRouter

routes_eg2 = APIRouter(prefix="/example2")

results_list = [
    "abcd",
    "abc",
    "ab",
    "a",
]

async def get_results(search_term):
    return [i for i in results_list if search_term in i]

@routes_eg2.get("/search/")
async def root(search_term: str = None) -> Dict[str, List[str]]:
    return {"output": await get_results(search_term)}



address_list = [
    "1 p g love av",
    "1 paanja av",
    "1 par cres",
    "1 park av",
    "1 park range way",
    "1 park rd",
    "2 park rd"
    "12 park rd"
]
@routes_eg2.get("/predict/address/")
async def root(search_term: str = None) -> Dict[str, List[str]]:
    return {"output": [i for i in address_list if search_term in i]}
