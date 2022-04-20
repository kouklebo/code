import pymysql
import pymysql.cursors
import os

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="Password123!",
    db="GLO_2005_projet",
    autocommit=True,
    local_infile=1
)
cursor = connection.cursor()


def read_sql(name):
    file = open(name, 'r')
    command = file.read()
    file.close()
    commands = command.split(';')
    for command in commands:
        cursor.execute(command)

try: read_sql("db_init.sql")
except (pymysql.err.OperationalError):
    pass

data_beersRequest = "LOAD DATA LOCAL INFILE %s INTO TABLE data_beers CHARACTER SET latin1  COLUMNS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '\"';"
data_customersRequest = "LOAD DATA LOCAL INFILE %s INTO TABLE data_customers CHARACTER SET latin1 COLUMNS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '\"';"
CreditCardRequest = "LOAD DATA LOCAL INFILE %s INTO TABLE credit_Card CHARACTER SET latin1 COLUMNS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '\"';"
data_beersFile = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data_beers.csv")
data_customerFile = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data_customers.csv")
CreditCardFile = os.path.join(os.path.dirname(os.path.abspath(__file__)), "CreditCard.csv")

cursor.execute(data_beersRequest, data_beersFile)
cursor.execute(data_customersRequest, data_customerFile)
cursor.execute(CreditCardRequest, CreditCardFile)
