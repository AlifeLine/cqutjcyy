import os

from flask import Flask
from flask_apscheduler import APScheduler
from flask_cors import CORS
from App.apis import init_api
from App.ext import init_ext
from App.settings import envs
from App.views import init_view
from datetime import timedelta


def create_app(env):
    app = Flask(__name__)
    # CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)
    app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))
    # 初始化项目配置
    app.config.from_object(envs.get(env))
    app.config['SESSION_COOKIE_NAME'] = 'token'
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(weeks=9999)
    app.config['SESSION_COOKIE_HTTPONLY'] = True
    app.config['SECRET_KEY'] = os.urandom(24)
    app.config['JSON_SORT_KEYS'] = False
    # 初始化 非路由相关的扩展
    init_ext(app)
    # 初始化api
    init_api(app)
    # 初始化路由
    init_view(app)
    return app
