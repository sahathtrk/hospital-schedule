import json
from typing import Any, Generic, Optional, TypeVar
from pydantic import BaseModel

DataType = TypeVar("DataType")


class IResponseBase(BaseModel, Generic[DataType]):
    message: str = "Success"
    meta: dict = {}
    data: Optional[DataType] = None
    code: str = "200000"
    error: Any = None



class IResponseBaseError(BaseModel, Generic[DataType]):
    message: str = "error"
    meta: dict = {}
    data: Optional[DataType] = None
    code: str = "code-error"
    error: Any = {}


responses = {
    500: {"model": IResponseBaseError, "description": "something error inside server"},
    400: {"model": IResponseBaseError, "description": "user request in bad format"},
    404: {"model": IResponseBaseError, "description": "item not found"},
    401: {"model": IResponseBaseError, "description": "user not authorized"},
    403: {"model": IResponseBaseError, "description": "forbidden action"},
}


def success_response(data: any, code: str = "200000", message: str = "Success") -> IResponseBase[Any]:
    return IResponseBase(data=data, code=code, message=message)


def error_response(error: any, code: str = "500000", message: str = "internal server error") -> IResponseBase[Any]:
    return IResponseBase(error=error, code=code, message=message)
