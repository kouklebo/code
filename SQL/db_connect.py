import pymysql
import configparser
import pymysql.cursors
import os

connection = configparser.ConfigParser()
connection.read('data.ini')
mySQLConnection = connection['MYSQL']
host, user, password, db = mySQLConnection['host'], \
                           mySQLConnection['user'], \
                           mySQLConnection['password'], \
                           mySQLConnection['db']

connection = pymysql.connect(
    host=host,
    user=user,
    password=password,
    db=db,
    autocommit=True)
cursor = connection.cursor()