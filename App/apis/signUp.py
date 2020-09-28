import os, random, string, uuid
import ast
from flask import Flask, request, jsonify, session, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from flask_restful import reqparse, abort, Api, Resource
from werkzeug.datastructures import FileStorage
import hashlib
import mimetypes
import time
import json
import datetime
import re
from flask.json import JSONEncoder
import shutil
import uuid
from flask_cors import CORS
from flask_restful import Resource, reqparse, abort, fields, marshal
from werkzeug.security import generate_password_hash, check_password_hash
import json
import werkzeug
from flask_apscheduler import APScheduler

from App.models.userInfo_model import UserInfo

parse_SignUp = reqparse.RequestParser()
parse_SignUp.add_argument("username", type=str, required=True)
parse_SignUp.add_argument("password", type=str, required=True)


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")


class SignInApi(Resource):
    def post(self):
        args = parse_SignUp.parse_args()
        # print(args)
        username = args.get("username")
        qdata = UserInfo.query.filter(UserInfo.username.__eq__(args.get("username"))).first()
        if qdata is not None:
            return jsonify({"code": 301, "msg": "用户名重复请更换用户名后重试"})
        password = args.get("password")
        # print(username, password)
        newUser = UserInfo()

        newUser.username = username
        newUser.password = generate_password_hash(password)
        if not newUser.save():
            newUser.rollback()
            return jsonify({"code": 301, "msg": "注册失败请稍后重试"})
        return jsonify({"code": 200, "msg": "注册成功"})
