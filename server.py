from flask import Flask, render_template, jsonify, request
from database import verif_mdp, select_table,ajout_compte

app = Flask(__name__)

VarGlobal = {}

@app.route("/")
def index():
    return render_template("Index.html")


@app.route("/magasin/", methods=["GET"])
def magasin():
    return render_template("Magasin.html")


@app.route("/compte/", methods=['GET', 'POST'])
def compte():
    global VarGlobal
    if request.method == 'POST':
        pseudo_user = request.form['pseudo_user']
        password = request.form['password']
        VarGlobal["pseudo"] = pseudo_user
        #print("password:",password, pseudo_user)
        Verif = verif_mdp(pseudo_user,password)
        #print("Verif:", Verif)
        if Verif == 1:
            return render_template("Compte.html",utilisateur=VarGlobal["pseudo"])
        else:
            #return 'Compte inconnu'
            return render_template("Compte.html")
    else:
        return render_template("Compte.html")

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

// Ajout dans le panier
@app.route("/panier/")
def panier():
    return render_template("Panier.html")

@app.route("/add-todo/", methods=["POST"])
def add_todo():
    data = request.json

    insert_todo(data["text"])

    response = {
        "status": 200
    }

    return jsonify(response)

@app.route("/contacter-nous/")
def contacter():
    return render_template("Contacter-nous.html")


@app.route("/tableMagasin/", methods=["GET"])
def get_table():
    tableMagasin = select_table()
    response = {
        "status": 200,
        "VectorMagasin": tableMagasin
    }
    return jsonify(response)


@app.route("/Achat/")
def achat():
    return render_template("Achat.html")

if __name__ == "__main__":
    app.run()
