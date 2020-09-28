import os, platform
from datetime import timedelta

from redis import StrictRedis


def get_db_uri(dbinfo):
    engine = dbinfo.get('ENGINE') or "mysql"
    driver = dbinfo.get('DRIVER') or "pymysql"
    user = dbinfo.get('USER') or "root"
    password = dbinfo.get('PASSWORD') or "root"
    host = dbinfo.get('HOST') or "localhost"
    port = dbinfo.get('PORT') or "3306"
    name = dbinfo.get('NAME') or "mtyuser"

    return "{}+{}://{}:{}@{}:{}/{}".format(engine, driver, user, password, host, port, name)


class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_TEARDOWN = True

    PERMANENT_SESSION_LIFETIME = timedelta(days=7)
    SECRET_KEY = os.urandom(24)
    SESSION_TYPE = "redis"


class DevelopConfig(Config):
    DEBUG = True
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = "6379"

    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "txm",
        "PASSWORD": "YA6AbpcpxCZL7KW6",
        "HOST": "10.0.1.211",
        "PORT": "3366",
        "NAME": "txm",
    }
    SCHEDULER_API_ENABLED = True
    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)


class TestingConfig(Config):
    TESTING = True
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = "6379"
    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "root",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "mtyuser",
    }
    SCHEDULER_API_ENABLED = True
    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)


class StagingConfig(Config):
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = "6379"
    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "root",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "mtyuser",
    }
    SCHEDULER_API_ENABLED = True
    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)


class ProductConfig(Config):
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = "6379"
    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "PayMent",
        "PASSWORD": "zh2kcBDdzT3BtaMA",
        "HOST": "127.0.0.1",
        "PORT": "3306",
        "NAME": "PayMent",
    }
    SCHEDULER_API_ENABLED = True
    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=False)


if platform.system() == "Windows":
    default = DevelopConfig
if platform.system() == "Linux":
    default = ProductConfig

envs = {
    "develop": DevelopConfig,
    "testing": TestingConfig,
    "staging": StagingConfig,
    "product": ProductConfig,
    "default": default
}
