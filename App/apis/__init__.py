from flask_restful import Api
from App.apis.signUp import SignInApi
from App.apis.Login import LoginApi
from App.apis.InfSetting import InfSettingApi

api = Api()


def init_api(app):
    api.init_app(app)


api.add_resource(SignInApi, '/apis/signup')
api.add_resource(LoginApi, '/apis/login')
api.add_resource(InfSettingApi, '/apis/InfSetting')
