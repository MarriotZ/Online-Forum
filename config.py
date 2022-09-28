# -*- coding: UTF-8 -*-  #指定文件编码格式
import  os

HOSTNAME = '127.0.0.1'
PORT     = '1433'
DATABASE = 'zhiHu'
USERNAME = 'yhc'
PASSWORD = '111111'
DB_URI = 'mssql+pymssql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
DEBUG = True

SECRET_KEY = os.urandom(24)