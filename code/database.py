import string
import pymysql.cursors
import csv
import hashlib

connection = pymysql.connect(
    host="localhost", user="root", password="Password123!", db="GLO_2005_projet", autocommit=True)

cursor = connection.cursor()


##
# \brief selection des biere
# \fn table def select_table():
# \return table de string
def select_table():
    request = "SELECT * FROM data_beers;"
    cursor.execute(request)

    table = [entry for entry in cursor.fetchall()]

    return table


##
# \brief selectionne les donnees de biere par type
# \fn select_style(query=None):
# \param query le type de biere ipa, rousse, blonde etc.
# \return table de string
def select_style(query=None):
    request = "SELECT * FROM data_beers"

    if query != "all":
        request += """ WHERE Style LIKE '%{}%'""".format(query)

    request += ";"

    cursor.execute(request)

    table_trie = [entry for entry in cursor.fetchall()]

    return table_trie


##
# \brief selectionne la commande des clients
# \fn def select_commande():
# \return table de string des commandes
def select_commande():
    request = "SELECT * FROM customer_Order;"
    cursor.execute(request)

    table = [entry for entry in cursor.fetchall()]

    return table

##
# \brief permet d inserer les commandes des clients dans le panier
# \fn def choix_panier(username, beer_id, quantity):
# \param username le nom d utilisateur du client
# \param beer_id le id de la biere acheter
# \param quantity la quantitee de biere achetee
def choix_panier(username, beer_id, quantity):
    request = """INSERT INTO customer_Order (Client_id , Beer_id , Quantity, Total_price)  VALUES ('{}', '{}', '{}',10);""".format(username, beer_id, quantity)
    cursor.execute(request)

##
# \brief verifie la validiter de l utilisateur
# \fn def verif_mdp(username, mdp):
# \param username ne nom d utilisateur de l usager
# \param mdp le mot de passe de l usager
# \return true or false si le l usager est valide ou non
def verif_mdp(username, mdp):
    request = "SELECT pseudo, motdepasse FROM pwd;"
    cursor.execute(request)

    for entry in cursor.fetchall():
        if username == entry[0] and mdp == entry[1]:
            return True
    return False

##
# \brief permet d ajouter un compte pour le client
# \fn ajout_compte(pseudo_user, name_user, first_name_user, birth_date_user, email_user, phone_number_user, Billing_address, Credit_card):
# \param speudo_user le nom d utilisateur
# \param name_user le prenom
# \param first_name_user son nom de famille
# \param birth_date_user sa date de naissance
# \param email_user son email
# \param phone_number_user son numeros de telephone
# \param Billing_address son addresse de credit
# \param Credit_card son numeros de carte de credit
# \return
def ajout_compte(pseudo_user, name_user, first_name_user, birth_date_user, email_user, phone_number_user, Billing_address, Credit_card):
    request = "INSERT INTO data_customers (pseudo, last_name, first_name, birth_date, email, phone_number, Billing_address,Credit_card)VALUES (%s, %s,%s,%s,%s,%s,%s,%s)"
    val = (pseudo_user, name_user, first_name_user, birth_date_user, email_user, phone_number_user, Billing_address,Credit_card)
    cursor.execute(request, val)
    Verification = 1
    print(Verification)
    return Verification

##
# \brief fonction servant a proteger les renseignement des usager
# \fn def hash_password(mot_de_passe_en_clair):
# \param password le mot de passe de l usager
# \return un mot de passe hacher
class HacheurDeMotDePasse:

    SEL_CRYPTO = "7f99fb781a504bb69b12fc4b58ce3414"

    @classmethod
    def hacher(cls, mot_de_passe_en_clair):

        return hashlib.sha512(mot_de_passe_en_clair.encode("utf-8") + cls.SEL_CRYPTO.encode("utf-8")).hexdigest()

    @classmethod
    def verifier(cls, hash_mot_de_passe, mot_de_passe_en_clair):

        return cls.hacher(mot_de_passe_en_clair) == hash_mot_de_passe

##
# \brief fonction servant a stocker les mot de passe et mot de passe hacher pour proteger les informations des usagers
# \fn def passwrd(pseudo_user):
# \param pseudo_user le speudonyme de l usager
# \return vrai ou faux si l usager est verifier par la fonction de hachage
def passwrd(pseudo_user):
    request = "INSERT INTO pwd (pseudo,motdepasse) VALUES (pseudo,mdp2)"
#  cursor.execute(request)
    Verification = 1
    return Verification

##
# \brief main
# \fn if __name__ == '__main__':
# \return un application web
if __name__ == '__main__':
    create_table = "CREATE TABLE Todo(id integer AUTO_INCREMENT text varchar(400), PRIMARY KEY(id))"
   # print(ajout_compte(1, 'Dupont', 'Jean', 19780106, 'jean.dupont@ulaval.ca', 1234567, '20 rue St Joseph','1234567890'));
