from werkzeug.security import check_password_hash, generate_password_hash

from App.ext import db


class Level():
    BLACK_USER = 0
    COMMON_USER = 1
    VIP_USER = 2
    MANAGER = 4
    SUPER_MANAGER = 8



