import datetime
from datetime import timedelta, datetime

from config import cfg
from dto import *
from model import *
from shared import ExceptionUnauthorized, success_response, IResponseBase, error_response
from utils import verify_password, create_access_token, create_password_hash
from utils.db import session
import uuid


def login_process(req: LoginRequest) -> AuthResponse:
    user_find = authenticate_user(req.email, req.password)
    time_expired = datetime.utcnow() + timedelta(minutes=cfg.jwt_expired_at)
    time_expired_refresh = datetime.utcnow() + timedelta(days=1)
    access_token = create_access_token({"email": user_find.email, "id": user_find.id, "role": user_find.role},
                                       cfg.jwt_token_secret, time_expired)
    refresh_token = create_access_token({"email": user_find.email},
                                        cfg.jwt_refresh_token_secret, time_expired_refresh)
    return AuthResponse(token=access_token, refresh_token=refresh_token,
                        expired_at=int(time_expired.timestamp() * 1000))

def register_process(request: RegisterRequest) -> any:
    user_query = session.query(UserTable)
    found_user = user_query.filter(UserTable.email == request.email).first()
    print(found_user)
    if found_user is None:
        new_user = UserTable(email=request.email,
                          id=uuid.uuid4(),
                          name=request.name,
                          password=create_password_hash(request.password),
                          phone_number=request.phone_number,
                          role=ROLE_PATIENT,)

        print(new_user)
        session.add(new_user)
        session.commit()
        return success_response(data="patient success registered")
    else:
        return error_response(error="email existed")



def authenticate_user(username: str, password: str) -> User:
    user_query = session.query(UserTable)
    found_user: UserTable = user_query.filter(UserTable.email == username).first()

    if found_user is None:
        raise ExceptionUnauthorized(code="401001", message="user not found")

    verify = verify_password(password, found_user.password)
    if not verify:
        raise ExceptionUnauthorized(code="401002", message="password  is wrong")
    return User.from_model_table(found_user)


def refresh_token_process(current_user: User):
    time_expired = datetime.utcnow() + timedelta(minutes=cfg.jwt_expired_at)
    time_expired_refresh = datetime.utcnow() + timedelta(days=1)
    access_token = create_access_token({"email": current_user.email, "id": current_user.id, "role": current_user.role},
                                       cfg.jwt_token_secret, time_expired)
    refresh_token = create_access_token({"email": current_user.email},
                                        cfg.jwt_refresh_token_secret, time_expired_refresh)
    return AuthResponse(token=access_token, refresh_token=refresh_token,
                        expired_at=int(time_expired.timestamp() * 1000))

