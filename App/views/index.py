from flask import Blueprint, jsonify, session

indexBlue = Blueprint('index_blue', __name__)

# app.config['SESSION_COOKIE_NAME'] = 'token'
from flask import render_template, request, Response, redirect, url_for
from App.models.userInfo_model import UserInfo


@indexBlue.route('/')
def index():
    if 'username' not in session:
        return redirect(url_for("login_blue.login"))
    qdata = UserInfo.query.filter(UserInfo.username.__eq__(session['username'])).first()
    if qdata.stuCode is None:
        return redirect(url_for("infoSetting_blue.infoSetting"))
    return redirect(url_for("choiceTxm_blue.choiceTxm"))
