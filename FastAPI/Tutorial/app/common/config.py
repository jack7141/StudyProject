from dataclasses import dataclass, asdict
from os import path, environ

base_dir = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))


@dataclass
class Config:
    """
    기본 Configuration
    """
    BASE_DIR = base_dir

    DB_POOL_RECYCLE: int = 900
    DB_ECHO: bool = True
    DB_URL: str = environ.get("DB_URL", "mysql+pymysql://admin:12341234@wanted-rds.cgish4s30zrj.us-east-1.rds.amazonaws.com:3306/wanted_api?charset=utf8mb4")


@dataclass
class LocalConfig(Config):
    PROJ_RELOAD: bool = True
    DB_URL: str = "mysql+pymysql://root:1234@localhost/wanted_api?charset=utf8mb4"


@dataclass
class ProdConfig(Config):
    PROJ_RELOAD: bool = False


def conf():
    """
    환경 불러오기
    :return:
    """
    config = dict(prod=ProdConfig(), local=LocalConfig())
    return config.get(environ.get("API_ENV", "prod"))
