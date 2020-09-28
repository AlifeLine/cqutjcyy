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

parse_infSetting = reqparse.RequestParser()
parse_infSetting.add_argument("name", type=str, required=True)
parse_infSetting.add_argument("stuCode", type=str, required=True)
parse_infSetting.add_argument("sex", type=str, required=True)
parse_infSetting.add_argument("email", type=str, required=True)
parse_infSetting.add_argument("idtype", type=str, required=True)
parse_infSetting.add_argument("zy", type=str, required=True)
parse_infSetting.add_argument("bj", type=str, required=True)
parse_infSetting.add_argument("clcc", type=str, required=True)
parse_infSetting.add_argument("bm", type=str, required=True)


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")


class InfSettingApi(Resource):
    def post(self):
        args = parse_infSetting.parse_args()
        # print(args)
        username = session['username']
        qdata = UserInfo.query.filter(UserInfo.username.__eq__(username)).first()
        if qdata is None:
            return jsonify({"code": 301, "msg": "登录失效请重新登录"})
        qdata.stuCode = args.get("stuCode")
        qdata.name = args.get("name")
        qdata.sex = args.get("sex")
        qdata.email = args.get("email")
        qdata.idtype = args.get("idtype")
        qdata.zy = args.get("zy")
        qdata.bj = args.get("bj")
        qdata.clcc = args.get("clcc")
        qdata.bm = args.get("bm")
        if not qdata.save():
            qdata.rollback()
            return jsonify({"code": 301, "msg": "更新信息失败"})
        return jsonify({"code": 200, "msg": "更新信息成功"})
