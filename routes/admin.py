from typing import Annotated

from fastapi import APIRouter, Depends

import controller
import middleware
import shared
from dto import UserResponse, adminRequest
from model import User, ROLE_ADMIN
from shared import IResponseBase, responses
from typing import Annotated

route_admin = APIRouter(
    prefix="/api/v1/admin",
    tags=["Admin"]
)


@route_admin.post("/add/nurse", response_model=IResponseBase[UserResponse], responses=responses)
async def add_nurse(request: adminRequest, current_user:Annotated[User, Depends(middleware.get_current_user)]):
    if(current_user.role == ROLE_ADMIN):
        return shared.success_response(data=controller.addNurse(request, current_user))
    else:
        return shared.error_response(message="try login as admin", code="403001", error='auth error')


@route_admin.post("/add/doctor", response_model=IResponseBase[UserResponse], responses=responses)
async def add_doctor(request: adminRequest, current_user:Annotated[User, Depends(middleware.get_current_user)]):
    if(current_user.role == ROLE_ADMIN):
        return shared.success_response(data=controller.addDoctor(request, current_user))
    else:
        return shared.error_response(message="try login as admin", code="403001", error='auth error')
