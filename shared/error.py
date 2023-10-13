from typing import Any

from fastapi import HTTPException, status
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from shared.response import error_response


class ExceptionCustom(HTTPException):
    code: str
    message: str
    cause: Any
    status_code: int

    def __init__(self, code: str = "500000", message: str = "error", cause: Any = None, status_code: int = 500):
        self.code = code
        self.message = message
        self.cause = cause
        super().__init__(status_code=status_code)


# 404
class ExceptionNotFound(ExceptionCustom):
    def __init__(self, code: str = "404000", message: str = "item not found", cause: Any = None):
        super().__init__(code, message, cause)


def exception_handler_not_found(request: Request, exc: ExceptionNotFound):
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=jsonable_encoder(error_response(
        error=exc.cause,
        code=exc.code,
        message=exc.message
    )))


# 400
class ExceptionBadRequest(ExceptionCustom):
    def __init__(self, code: str = "400000", message: str = "bad request", cause: Any = None):
        super().__init__(code, message, cause)


def exception_handler_bad_request(request: Request, exc: ExceptionBadRequest):
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=jsonable_encoder(error_response(
        error=exc.cause,
        code=exc.code,
        message=exc.message
    )))


# 500
class ExceptionInternalServerError(ExceptionCustom):
    def __init__(self, code: str = "500000", message: str = "internal server error", cause: Any = None):
        super().__init__(code, message, cause)


def exception_handler_internal_server_error(request: Request, exc: ExceptionInternalServerError):
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=jsonable_encoder(error_response(
        error=exc.cause,
        code=exc.code,
        message=exc.message
    )))


# 401
class ExceptionUnauthorized(ExceptionCustom):
    def __init__(self, code: str = "401000", message: str = "bad request", cause: Any = None):
        super().__init__(code, message, cause)


def exception_handler_unauthorized(request: Request, exc: ExceptionUnauthorized):
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=jsonable_encoder(error_response(
        error=exc.cause,
        code=exc.code,
        message=exc.message
    )))


# 403
class ExceptionForbidden(ExceptionCustom):
    def __init__(self, code: str = "403000", message: str = "forbidden", cause: Any = None):
        super().__init__(code, message, cause)


def exception_handler_forbidden(request: Request, exc: ExceptionForbidden):
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=jsonable_encoder(error_response(
        error=exc.cause,
        code=exc.code,
        message=exc.message
    )))
