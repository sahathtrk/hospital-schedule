from datetime import datetime

from fastapi.security import OAuth2PasswordBearer
from jose import jwt

from config import cfg

ALGORITHM = "HS256"

def create_access_token(data: dict, secret: str = cfg.jwt_token_secret, expires: datetime = None, ):
    to_encode = data.copy()
    to_encode.update({"exp": expires})
    encoded_jwt = jwt.encode(to_encode, secret, algorithm=ALGORITHM)
    return encoded_jwt
