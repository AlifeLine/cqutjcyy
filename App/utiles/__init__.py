import pymysql, platform

if platform.system() == "Windows":
    data = pymysql.connect(host="47.113.113.143", port=3306, user="UserInfo", password="kYGNarjMZbFSLrGr",
                           db="UserInfo",
                           charset="utf8")
if platform.system() == "Linux":
    data = pymysql.connect(host="127.0.0.1", port=3306, user="UserInfo", password="kYGNarjMZbFSLrGr", db="UserInfo",
                           charset="utf8")
cursor = data.cursor()
