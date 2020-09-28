from App.views.Txm import TxmBlue
from App.views.index import indexBlue
from App.views.login import loginBlue
from App.views.showMsg import msgBlue
from App.views.infSetting import infoSettingBlue
from App.views.choiceTxm import choiceTxmBlue


# from App.views.index import index_blue

def init_view(app):
    app.register_blueprint(indexBlue)
    app.register_blueprint(TxmBlue)
    app.register_blueprint(loginBlue)
    app.register_blueprint(msgBlue)
    app.register_blueprint(choiceTxmBlue)
