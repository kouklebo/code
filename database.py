import pymysql.cursors

connection = pymysql.connect(
    host="localhost", user="root", password="", db="GLO_2005_projet", autocommit=True)

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


def create_pwd():
    request = "CREATE TABLE Pwd(pseudo VARCHAR(100),motdepasse VARCHAR(100),PRIMARY KEY (pseudo))"
    cursor.execute(request)


def insert_pwd(pseudo,motdepasse):
    request = """INSERT INTO pwd (pseudo,motdepasse) VALUES ("{}","{}");""".format(pseudo,motdepasse)
    cursor.execute(request)


def verif_mdp(username,mdp):
    request= "SELECT pseudo, motdepasse FROM pwd;"
    cursor.execute(request)

    list_mdp = [(entry[0],entry[1]) for entry in cursor.fetchall()]


    #for entry in cursor.fetchall():
       # if username==entry[0] and mdp==entry[1]:
       #     return print("identite_confirme")
     #   else :
     #       return print("Compte inconnu")
    return list_mdp


def delete_pwd():
    request = "DROP TABLE Pwd"
    cursor.execute(request)


if __name__ == '__main__':
    # create_table = "CREATE TABLE Todo(id integer AUTO_INCREMENT,"\
    #  text varchar(400), PRIMARY KEY(id))"
    # cursor.execute(create_table)
    #delete_pwd()
    #create_pwd()
    #insert_pwd("Jennifer1","mdp1")
    print(verif_mdp('Jennifer1',"mdp1"))
