from typing import Annotated

from fastapi import APIRouter, Depends

import controller
import middleware
import shared
from dto import AuthResponse, LoginRequest, RegisterRequest
from model import User
from shared import IResponseBase, responses

route_auth = APIRouter(
    prefix="/api/v1/auth",
    tags=["Auth"]
)


@route_auth.post("/login", response_model=IResponseBase[AuthResponse], responses=responses)
async def login(request: LoginRequest):
    return shared.success_response(data=controller.login_process(request))


@route_auth.post("/refresh", response_model=IResponseBase[AuthResponse], responses=responses)
async def refresh(
        current_user: Annotated[User, Depends(middleware.get_current_user_refresh)]
):
    return shared.success_response(data=controller.refresh_token_process(current_user))


@route_auth.post("/register", response_model=IResponseBase, responses=responses)
async def register(request: RegisterRequest):
    return controller.register_process(request)
