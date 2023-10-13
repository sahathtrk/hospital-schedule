from typing import Annotated

from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError

import shared
import utils
from config import cfg
from model import UserTable, User
from utils.db import session

oauth2_scheme = HTTPBearer()


async def get_current_user(token: HTTPAuthorizationCredentials = Depends(oauth2_scheme)) -> User:
    try:
        payload = jwt.decode(token.credentials, cfg.jwt_token_secret, algorithms=[utils.ALGORITHM])
        user_id: str = payload.get("id")
        if user_id is None:
            raise shared.ExceptionForbidden(code="403001", message="bearer token is invalid")
        user_query = session.query(UserTable)
        user = user_query.filter(UserTable.id == user_id).first()
        if user is None:
            raise shared.ExceptionForbidden(code="403003", message="bearer token is invalid")
        return User.from_model_table(user)
    except JWTError:
        raise shared.ExceptionForbidden(code="403002", message="bearer token is invalid")


async def get_current_user_refresh(token: HTTPAuthorizationCredentials = Depends(oauth2_scheme)) -> User:
    try:
        payload = jwt.decode(token.credentials, cfg.jwt_refresh_token_secret, algorithms=[utils.ALGORITHM])
        user_id: str = payload.get("email")
        if user_id is None:
            raise shared.ExceptionForbidden(code="403001", message="bearer token is invalid")
        user_query = session.query(UserTable)
        user = user_query.filter(UserTable.email == user_id).first()
        if user is None:
            raise shared.ExceptionForbidden(code="403003", message="bearer token is invalid")
        return User.from_model_table(user)
    except JWTError:
        raise shared.ExceptionForbidden(code="403002", message="bearer token is invalid")
