from fastapi import APIRouter

from dto import ResponseHello
from shared import *

route_home = APIRouter(
    prefix="/home",
    tags=["Home"]
)


@route_home.get("/hello/{name}", response_model=IResponseBase[ResponseHello],
                responses=responses)
async def say_hello(name: str):
    if name == "Andree":
        raise ExceptionBadRequest(code="500020")
    return success_response(data=ResponseHello(name=name, message=f"Hello {name}"))
