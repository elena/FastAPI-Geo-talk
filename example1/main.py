"""
Example:

Basic path variable input.
"""
from fastapi import APIRouter

routes_eg1 = APIRouter(prefix="/example1")

@routes_eg1.get("/")
async def root():
    return {"message": "Hello World"}


@routes_eg1.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
