from flask import Blueprint, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

infoSettingBlue = Blueprint('infoSetting_blue', __name__)

# app.config['SESSION_COOKIE_NAME'] = 'token'
from flask import render_template, request, Response, redirect, url_for
from datetime import datetime


# from App.models.billTable_model import BillTable
# from App.models.userInfo_model import UserInfo


@infoSettingBlue.route('/infoSetting')
def infoSetting():
    return render_template("infoSetting.html")
