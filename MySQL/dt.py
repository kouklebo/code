import pymysql

connection = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'gribouille',
    db = 'projet_glo_2005'
    autocommit = TRUE
)

cursor = connection.cursor()