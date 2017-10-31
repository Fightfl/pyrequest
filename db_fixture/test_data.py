__author__ = 'lihao'
# -*- coding: utf-8 -*-
import sys
sys.path.append('../db_fixture')
try:
    from mysql_db import DB
except ImportError:
    from .mysql_db import DB

# create data
datas = {
    'sign_guest':[
        {'id':1,'realname':'alen','phone':13511001100,'email':'alen@mail.com','sign':0,'event_id':1,'create_time':'2017-10-31 14:00:00'},
        {'id':2,'realname':'has sign','phone':13511001101,'email':'sign@mail.com','sign':1,'event_id':1,'create_time':'2017-10-31 14:00:00'},
        {'id':3,'realname':'tom','phone':13511001102,'email':'tom@mail.com','sign':0,'event_id':5,'create_time':'2017-10-31 14:00:00'},
    ],
}

# Insert table datas
def init_data():
    DB().init_data(datas)

if __name__ == '__main__':
    init_data()