from fastapi import APIRouter

routes_eg2 = APIRouter(prefix="/example2")

show_list = [
    "abcd",
    "zabc",
    "yzab",
    "xyza",
]

@routes_eg2.get("/search/")
async def root(search_term: str = None) -> dict[str, list[str]]:
    return {"output": [i for i in show_list if search_term in i]}



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
async def root(search_term: str = None) -> dict[str, list[str]]:
    return {"output": [i for i in address_list if search_term in i]}
