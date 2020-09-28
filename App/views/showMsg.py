from flask import Blueprint, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

msgBlue = Blueprint('msg_blue', __name__)

# app.config['SESSION_COOKIE_NAME'] = 'token'
from flask import render_template, request, Response, redirect, url_for
from datetime import datetime


# from App.models.billTable_model import BillTable
# from App.models.userInfo_model import UserInfo


@msgBlue.route('/showMsg')
def show_message():
    return render_template("message.html", message=request.args.get("msg"))
