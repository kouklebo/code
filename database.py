import pymysql.cursors

connection = pymysql.connect(
    host="localhost", user="root", password="root", db="GLO_2005_projet", autocommit=True)

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

def ajout_compte(pseudo_user, name_user, firt_name_user, birth_date_user, email_user, phone_number_user, Billing_address,Credit_card):
    request= "INSERT INTO data_customers (pseudo, last_name, first_name, birth_date, email, phone_number, Billing_address,Credit_card) VALUES (3, 'name_user', 'firt_name_user', 20230608, 'email_user', 1234567, 'Billing_address',1234567890);"
    cursor.execute(request)
    Verification = 1
    print(Verification)
    return Verification

def passwrd(pseudo_user):
    request= "INSERT INTO pwd (pseudo,motdepasse) VALUES (pseudo,mdp2)"
    cursor.execute(request)
    Verification = 1
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
    print(ajout_compte(3,'Dupont', 'Jean',19780106,'jean.dupont@ulaval.ca',1234567,'20 rue St Joseph','1234567890'));