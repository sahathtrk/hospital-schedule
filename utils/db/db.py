from sqlalchemy import URL, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from config import *

url = URL.create(
    host=cfg.db_host,
    username=cfg.db_user,
    password=cfg.db_password,
    database=cfg.db_name,
    drivername="mysql+pymysql",
    port=cfg.db_port
)
engine = create_engine(url)
Session = sessionmaker(bind=engine, autoflush=False)
session = Session()
base = declarative_base()
