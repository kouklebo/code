from flask import Flask, render_template, jsonify, request
from database import verif_mdp, select_table, ajout_compte, choix_panier, select_style, select_commande

app = Flask(__name__)

##
# \brief route de l index ie la page principale
# \fn def index():
# \return html du template de l index.html
@app.route("/")
def index():
    return render_template("Index.html")

##
# \brief route du magasin
# \fn def magasin():
# \return html du template du magasin.html
@app.route("/magasin/", methods=["GET"])
def magasin():
    return render_template("Magasin.html")


##
# \brief route pour la demande de tries de type de biere ipa, rousse blonde etc.
# \fn def tri_style():
# \return json des donnees de type de biere
@app.route("/magasin/style/", methods=["GET"])
def tri_style():
    query = request.args.get("query")

    todos = select_style(query)

    response = {
        "status": 200,
        "todos": todos
    }

    return jsonify(response)


##
# \brief sert a aller chercher les donnees du panier
# \fn def commande():
# \return json des donnees contenue dans le panier
@app.route("/panier_commande/", methods=["GET"])
def commande():
    #probleme a cause de la variable globale de javascrip
    #on aurait du utiliser url mais on ne le savais pas au debut
    # peut etre ameliorer en utilisant url
    user = request.args.get("user")
    print (user)
    todos = select_commande()

    response = {
        "status": 200,
        "todos": todos
    }

    return jsonify(response)


##
# \brief route du compte
# \fn def compte():
# \return html du template du compte.html
@app.route("/compte/", methods=['GET', 'POST'])
def compte():
    return render_template("Compte.html")


##
# \brief verifie les donner entrer par usager
# \fn def compte_verif():
# \return une route vers une page html contenant les caracteres
#compte inconnue ou connexion reussit
@app.route("/compte_verif/", methods=['GET', 'POST'])
def compte_verif():
    if request.method == 'POST':
        pseudo_user = request.form['pseudo_user']
        password = request.form['password']

        if verif_mdp(pseudo_user, password):
            return 'Connexion reussit'
        else:
            return 'Compte inconnu'


##
# \brief renvoie le pseudo de l usager si le mot de passe est verifier
#devrait etre utiliser avec url
# \fn def compte_login():
# \return json contenant l usager
@app.route("/compte_login/", methods=['GET', 'POST'])
def compte_login():
    if request.method == 'POST':
        data = request.json

        if verif_mdp(data["pseudo_user"], data["password"]):
            response = {
                "status": 200,
                "pseudo_user": data["pseudo_user"]
            }
        else:
            response = {
                "status": 200,
                "pseudo_user": None
            }
        return jsonify(response)


##
# \brief permet denvoyer les donnees vers la database quand on cree un compte
# \fn def creation_compte():
# \return un message si cela fonctionne ou non
@app.route("/creation_compte/", methods=['GET', 'POST'])
def creation_compte():
    if request.method == 'POST':
        nom_user = request.form['nom_user']
        prenom_user = request.form['prenom_user']
        naissance_user = request.form['naissance_user']
        pseudo_user = request.form['pseudo_user']
        courriel = request.form['courriel']
        num_telephone = request.form['num_telephone']
        adresse = request.form['adresse']
        num_carte = request.form['num_carte']
        #print("password:",password, pseudo_user)
        #passwrd= creation_mdp(pseudo_user)
        Ajout = ajout_compte(pseudo_user,nom_user,prenom_user,naissance_user,courriel,num_telephone,adresse,num_carte)
        #print("Verif:", Verif)
        #if Ajout == 1 and passwrd==1:
        if Ajout == 1:
            return 'Compte Crée. Bienvenue !  Votre mot de passe vous sera envoyé par mail.'
        else:
            return 'Une erreure est survenue. Merci de vérifier le contenu des champs.'
    else:
        return render_template("Compte.html")


##
# \brief route du panier
# \fn def panier():
# \return html du template du panier.html
@app.route("/panier/")
def panier():
    return render_template("Panier.html")


##
# \brief envoie les donnees des commandes du client a la database
# \fn def choix_todo():
# \return envoie les donnees a la database pour les commandes
@app.route("/choixPanier/", methods=["POST"])
def choix_todo():
    data = request.json
    choix_panier(data["username"], data["beer_id"], data["quantity"])
    response = {
        "status": 200
    }
    return jsonify(response)


##
# \brief route de la page contacter-nous
# \fn def contacter-nous():
# \return html du template du contacter-nous.html
@app.route("/contacter-nous/")
def contacter():
    return render_template("Contacter-nous.html")


##
# \brief route pour les donnees des bieres
# \fn def get_table():
# \return json des donnes des bieres
@app.route("/tableMagasin/", methods=["GET"])
def get_table():
    tableMagasin = select_table()
    response = {
        "status": 200,
        "VectorMagasin": tableMagasin
    }
    return jsonify(response)


##
# \brief route de la page Achat
# \fn def achat():
# \return html du template du Achat.html
@app.route("/Achat/")
def achat():
    return render_template("Achat.html")


##
# \brief main
# \return application web
if __name__ == "__main__":
    app.run()


