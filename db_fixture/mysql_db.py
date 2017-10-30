__author__ = 'lihao'
# coding=utf8
from pymysql import connect, cursors
from pymysql.err import OperationalError
import os
import configparser as cparser

#==========读取db_config.ini文件设置=========
base_dir = str(os.path.dirname(os.path.dirname(__file__)))
base_dir = base_dir.replace('\\', '/')
file_path = base_dir + "/db_config.ini"

cf = cparser.ConfigParser()
cf.read(file_path)

host = cf.get("mysqlconf", "host")
port = cf.get("mysqlconf", "port")
db = cf.get("mysqlconf", "db_name")
user = cf.get("mysqlconf", "user")
password = cf.get("mysqlconf", "password")
