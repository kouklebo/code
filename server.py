from flask import Flask, render_template, jsonify, request
from database import verif_mdp, select_table

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("Index.html")


@app.route("/magasin/")
def magasin():
    return render_template("Magasin.html")


@app.route("/compte/", methods=['GET', 'POST'])
def compte():
    if request.method == 'POST':
        pseudo_user = request.form['pseudo_user']
        password = request.form['password']
        print("password:",password, pseudo_user)
        Verif = verif_mdp(pseudo_user,password)
        print("Verif:", Verif)
        if Verif == 1:
            return 'Compte existant'
        else:
            return 'Compte inconnu'
    else:
        return render_template("Compte.html")


@app.route("/panier/")
def panier():
    return render_template("Panier.html")


@app.route("/contacter-nous/")
def contacter():
    return render_template("Contacter-nous.html")


@app.route("/uneTable/", methods=["GET"])
def get_table():
    table = select_table()

    response = {
        "status": 200,
        "xtable": table
    }
    return jsonify(response)


if __name__ == "__main__":
    app.run()
