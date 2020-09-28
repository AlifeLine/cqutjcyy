from flask import Blueprint, jsonify, session

try:
    import cPickle as pickle
except ImportError:
    import pickle

TxmBlue = Blueprint('Txm_blue', __name__)

# app.config['SESSION_COOKIE_NAME'] = 'token'
from flask import render_template, request, Response, redirect, url_for
from datetime import datetime
import random
# from App.models.billTable_model import BillTable
# from App.models.WeChatUser_model import WeChatUser
from App.models.userInfo_model import UserInfo


def getidCard():
    return ''.join(random.choice(["5002", "5102", "3201"]) for _ in range(1)) + "******" + ''.join(
        random.choice('0123456780') for _ in range(4))


@TxmBlue.route('/getTxm')
def getTxm():
    if "username" not in session:
        return redirect(url_for("login_blue.login"))
    location = request.args.get("location")
    inout = request.args.get("inout")
    qdata = UserInfo.query.filter(UserInfo.username.__eq__(session['username'])).first()
    return render_template("student.html", stuCode=qdata.stuCode, stuname=qdata.name, sex=qdata.sex, type=qdata.idtype,
                           mb=qdata.bm,
                           zy=qdata.zy, bj=qdata.bj, cc=qdata.clcc, sfzhm=getidCard(), gxgt=location, txsj=inout)
