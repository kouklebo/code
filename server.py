from flask import Flask, render_template, jsonify, request
from database import select_table #,verif_mdp, insert_todo, select_todos

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("Index.html")


@app.route("/magasin/")
def magasin():
    return render_template("Magasin.html")


@app.route("/compte/")
def compte():
    return render_template("Compte.html")


@app.route("/panier/")
def panier():
    return render_template("Panier.html")


@app.route("/contacter-nous/")
def contacter():
    return render_template("Contacter-nous.html")


#@app.route("/verif_compte/",methods=["GET"])
#def get_compte():
   # verif =verif_mdp()
   # response={
    #    "status":200,
     #   "verif":verif_mdp()
   # }
   # return jsonify(response)


#@app.route("/todos/", methods=["GET"])
#def get_todos():
#    todos = select_todos()
#
#    response = {
#        "status": 200,
#        "todos": todos
#    }
#    return jsonify(response)


@app.route("/uneTable/", methods=["GET"])
def get_table():
    table = select_table()

    response = {
        "status": 200,
        "xtable": table
    }
    return jsonify(response)


if __name__ == "__main__":

    print(select_table())

    app.run()



