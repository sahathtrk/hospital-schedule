from typing import Annotated

from fastapi import APIRouter, Depends

import middleware
from model import User
from shared import responses, IResponseBase

route_user = APIRouter(
    prefix="/api/v1/users",
    tags=["Users"]
)


@route_user.get("/me", response_model=IResponseBase[User], responses=responses)
async def get_me(
        current_user: Annotated[User, Depends(middleware.get_current_user)]
):
    return IResponseBase[User](data=current_user)
