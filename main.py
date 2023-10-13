import uuid

import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

import model
from config import cfg
from routes import *
from shared import *
from utils.db import session, base, engine
from utils import create_password_hash

app = FastAPI()

base.metadata.create_all(engine)

# Insert admin user if not exist
query_user = session.query(model.UserTable)
found_user = query_user.filter(model.UserTable.email == cfg.email_admin).first()
if found_user is None:
    new_user = model.UserTable(email=cfg.email_admin,
                          id=uuid.uuid4(),
                          name="Admin User",
                          password=create_password_hash(cfg.password_admin),
                          phone_number="08121231414",
                          role=model.ROLE_ADMIN,
                          )
    session.add(new_user)
    session.commit()

app.add_exception_handler(ExceptionNotFound, exception_handler_not_found)
app.add_exception_handler(ExceptionInternalServerError, exception_handler_internal_server_error)
app.add_exception_handler(ExceptionUnauthorized, exception_handler_unauthorized)
app.add_exception_handler(ExceptionForbidden, exception_handler_forbidden)
app.add_exception_handler(ExceptionBadRequest, exception_handler_bad_request)


@app.exception_handler(404)
async def not_found_exception_handler(request: Request, exc: HTTPException):
    return RedirectResponse('https://fastapi.tiangolo.com')


app.include_router(route_home)
app.include_router(route_user)
app.include_router(route_auth)
app.include_router(route_admin)
app.include_router(route_doctor)
app.include_router(route_nurse)
app.include_router(route_patient)