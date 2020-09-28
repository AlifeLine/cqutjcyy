from flask import Blueprint, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash

choiceTxmBlue = Blueprint('choiceTxm_blue', __name__)

# app.config['SESSION_COOKIE_NAME'] = 'token'
from flask import render_template, request, Response, redirect, url_for
from datetime import datetime


# from App.models.billTable_model import BillTable
# from App.models.userInfo_model import UserInfo


@choiceTxmBlue.route('/choiceTxm')
def choiceTxm():
    if "username" not in session:
        return redirect(url_for("login_blue.login"))
    return render_template("choice.html")
