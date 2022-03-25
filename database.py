import pymysql.cursors

connection = pymysql.connect(
    host="localhost", user="root", password="Password123#@!", db="glo_2005_webapp", autocommit=True)

cursor = connection.cursor()


def insert_todo(text):
    request = """INSERT INTO Todo (text) VALUES ("{}");""".format(text)
    cursor.execute(request)


def select_todos():
    request = "SELECT text FROM Todo;"
    cursor.execute(request)

    todos = [entry[0] for entry in cursor.fetchall()]

    return todos


def select_table():
    request = "SELECT * FROM data_beers;"
    cursor.execute(request)

    table = [entry[0] for entry in cursor.fetchall()]

    return table


if __name__ == '__main__':
    create_table = "CREATE TABLE Todo(id integer AUTO_INCREMENT, text varchar(400), PRIMARY KEY(id))"
    cursor.execute(create_table)
