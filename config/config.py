import os

from dotenv import load_dotenv


class Config:
    def __init__(self):
        load_dotenv()

        # Server Env
        self.server_host = os.getenv("SERVER_HOST")
        self.server_port = os.getenv("SERVER_PORT")

        # DB Env
        self.db_host = os.getenv("DB_HOST")
        self.db_port = int(os.getenv("DB_PORT"))
        self.db_user = os.getenv("DB_USER")
        self.db_password = os.getenv("DB_PASSWORD")
        self.db_name = os.getenv("DB_NAME")

        # Token
        self.jwt_token_secret = os.getenv("JWT_TOKEN_SECRET")
        self.jwt_expired_at = int(os.getenv("JWT_EXPIRED_AT"))
        self.jwt_refresh_token_secret = os.getenv("JWT_REFRESH_TOKEN_SECRET")

        # Hashed
        self.hashed_secret = os.getenv("HASHED_SECRET")
        self.password_admin = os.getenv("PASSWORD_ADMIN")
        self.email_admin = os.getenv("EMAIL_ADMIN")


cfg = Config()
