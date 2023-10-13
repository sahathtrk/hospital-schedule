from pydantic import BaseModel


class ResponseHello(BaseModel):
    name: str
    message: str
