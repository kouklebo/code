from flask import Flask, render_template, jsonify, request
from database import insert_todo, select_todos #,select_table #,verif_mdp

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


#@app.route("/magasin/")
#def magasin():
#    return render_template("Magasin.html")


@app.route("/add-todo/", methods=["POST"])
def add_todo():
    data = request.json

    insert_todo(data["text"])

    response = {
        "status": 200
    }

    return jsonify(response)

#@app.route("/verif_compte/",methods=["GET"])
#def get_compte():
   # verif =verif_mdp()
   # response={
    #    "status":200,
     #   "verif":verif_mdp()
   # }
   # return jsonify(response)


@app.route("/todos/", methods=["GET"])
def get_todos():
    todos = select_todos()

    response = {
        "status": 200,
        "todos": todos
    }
    return jsonify(response)

#@app.route("/table/", methods=["GET"])
#def get_table():
#    table = select_table()
#
#    response = {
#        "status": 200,
#        "table": table
#    }
#    return jsonify(response)


if __name__ == "__main__":
    app.run()



