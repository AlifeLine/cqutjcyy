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

parse_Login = reqparse.RequestParser()
parse_Login.add_argument("username", type=str, required=True)
parse_Login.add_argument("password", type=str, required=True)


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")



class LoginApi(Resource):
    def post(self):
        args = parse_Login.parse_args()
        # print(args)
        username = args.get("username")
        qdata = UserInfo.query.filter(UserInfo.username.__eq__(username)).first()
        if qdata is None:
            return jsonify({"code": 301, "msg": "用户名不存在"})
        password = args.get("password")
        if check_password_hash(qdata.password, password):
            session['username'] = username
            # session['name'] = qdata.name
            session['stuCode'] = qdata.stuCode
            # session['email'] = qdata.email
            # session['idtype'] = qdata.idtype
            # session['sex'] = qdata.sex
            # session['bm'] = qdata.bm
            # session['zy'] = qdata.zy
            # session['bj'] = qdata.bj
            # session['clcc'] = qdata.clcc
            session.permanent = True
            return jsonify({"code": 200, "msg": "登录成功"})
        return jsonify({"code": 301, "msg": "密码错误"})
