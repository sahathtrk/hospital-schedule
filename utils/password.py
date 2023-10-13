from passlib.context import CryptContext

from config import cfg

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto", ldap_salted_md5__salt_size=16)


def create_password_hash(password):
    return pwd_context.hash(password)


def verify_password(password, hashed_password):
    return pwd_context.verify(password, hashed_password)

