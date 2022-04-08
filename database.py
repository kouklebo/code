import string
import pymysql.cursors
import csv


connection = pymysql.connect(
    host="localhost", user="root", password="root", db="GLO_2005_projet", autocommit=True)

cursor = connection.cursor()


def select_table():
    request = "SELECT * FROM data_beers;"
    cursor.execute(request)

    table = [entry for entry in cursor.fetchall()]

    return table


def choix_panier(username, beer_id, quantity):
    request = """INSERT INTO customer_Order (Order_id, Client_id , Beer_id , Quantity, Total_price)  VALUES (2,'{}', '{}', '{}',10);""".format(username, beer_id, quantity)
    cursor.execute(request)


def verif_mdp(username, mdp):
    request = "SELECT pseudo, motdepasse FROM pwd;"
    cursor.execute(request)

    Verification = -1
    for entry in cursor.fetchall():
        if username == entry[0] and mdp == entry[1]:
            return True
    return False


def ajout_compte(pseudo_user, name_user, first_name_user, birth_date_user, email_user, phone_number_user, Billing_address, Credit_card):
    request = "INSERT INTO data_customers (pseudo, last_name, first_name, birth_date, email, phone_number, Billing_address,Credit_card)VALUES (%s, %s,%s,%s,%s,%s,%s,%s)"
    val = (pseudo_user, name_user, first_name_user, birth_date_user, email_user, phone_number_user, Billing_address,Credit_card)
    cursor.execute(request, val)
    Verification = 1
    print(Verification)
    return Verification


#def passwrd(pseudo_user):
 #   request = "INSERT INTO pwd (pseudo,motdepasse) VALUES (pseudo,mdp2)"
  #  cursor.execute(request)
    #Verification = 1
    #return Verification


if __name__ == '__main__':
    create_table = "CREATE TABLE Todo(id integer AUTO_INCREMENT text varchar(400), PRIMARY KEY(id))"
   # print(ajout_compte(1, 'Dupont', 'Jean', 19780106, 'jean.dupont@ulaval.ca', 1234567, '20 rue St Joseph','1234567890'));
