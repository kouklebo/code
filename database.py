import pymysql.cursors

connection = pymysql.connect(
    host="localhost", user="root", password="Password123#@!", db="GLO_2005_projet", autocommit=True)

cursor = connection.cursor()


def select_table():
    request = "SELECT * FROM data_beers;"
    cursor.execute(request)

    table = [entry for entry in cursor.fetchall()]

    return table


#def create_pwd():
#    request = "CREATE TABLE Pwd(pseudo VARCHAR(100),motdepasse VARCHAR(100),PRIMARY KEY (pseudo))"
#    cursor.execute(request)


#def insert_pwd(pseudo,motdepasse):
 #   request = """INSERT INTO pwd (pseudo,motdepasse) VALUES ("{}","{}");""".format(pseudo,motdepasse)
  #  cursor.execute(request)


def verif_mdp(username,mdp):
    request= "SELECT pseudo, motdepasse FROM pwd;"
    cursor.execute(request)

    Verification = -1
    for entry in cursor.fetchall():
        if username==entry[0] and mdp==entry[1]:
            Verification=1
            print('Verification',Verification)
        else :
            Verification=0
            print('Verification', Verification)
        return Verification
    return Verification


#def delete_pwd():
  #  request = "DROP TABLE Pwd"
   # cursor.execute(request)


if __name__ == '__main__':
    create_table = "CREATE TABLE Todo(id integer AUTO_INCREMENT text varchar(400), PRIMARY KEY(id))"
    #cursor.execute(create_table)
    #delete_pwd()
    #create_pwd()
    #insert_pwd("Jennifer1","mdp1")
    #print(verif_mdp('Jennifer1',"mdp1"))
