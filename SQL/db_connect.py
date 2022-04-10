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

db = pymysql.connect(
    host=host,
    user=user,
    password=password,
    db=db,
    autocommit=True)
mycursor = db.cursor()

def readSQLcommand(name):
    file = open(name, 'r')
    sqlcommand = file.read()
    file.close()

    sqlCommands = sqlcommand.split(';')

    for i in sqlCommands:
        mycursor.execute(i)

try:
    readSQLcommand("db_init.sql")
except (pymysql.err.InternalError):
    pass

data_beersRequest = "LOAD DATA INFILE %s INTO TABLE data_beers " \
                    "COLUMNS TERMINATED BY ','" \
                    "OPTIONALLY ENCLOSED BY '\"';"

data_customersRequest = "LOAD DATA INFILE %s INTO TABLE data_customers " \
                    "COLUMNS TERMINATED BY ','" \
                    "OPTIONALLY ENCLOSED BY '\"';"

CreditCardRequest = "LOAD DATA INFILE %s INTO TABLE credit_card " \
                    "COLUMNS TERMINATED BY ','" \
                    "OPTIONALLY ENCLOSED BY '\"';"


data_beersFile = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data_beers.csv")
data_customerFile = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data_customers.csv")
CreditCardFile = os.path.join(os.path.dirname(os.path.abspath(__file__)), "CreditCard.csv")

mycursor.execute(data_beersRequest, data_beersFile)
mycursor.execute(data_customersRequest, data_customerFile)
mycursor.execute(CreditCardRequest, CreditCardFile)
