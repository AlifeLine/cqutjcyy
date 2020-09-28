from flask_caching import Cache
from flask_jwt import JWT
from flask_migrate import Migrate
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_qrcode import QRcode

db = SQLAlchemy()
migrate = Migrate()
csrf = CSRFProtect()
jwt = JWT()
cache = Cache(config={
    "CACHE_TYPE": "simple"
})


def init_ext(app):
    db.init_app(app)
    migrate.init_app(app, db)
    cache.init_app(app)
    Session(app)
    QRcode(app)
