import os

class Config:
    DATABASE_URL = os.getenv("DATABASE_URL", "mysql+mysqlconnector://root:root@localhost:3306/open_boxe")
    SECRET_KEY = os.getenv("SECRET_KEY", "chave-secreta-super-segura-para-jwt")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30