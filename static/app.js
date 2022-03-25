/*function displayNewTodo(text) {
    var name_user = document.getElementById("info_user")

    var nom_user = document.createElement("div")

    nom_user.innerHTML = text;

    name_user.appendChild(nom_user);
}

function onButtonClick() {
    var inputname = document.getElementById("pseudo_user")

    var newname = inputname.value

    displayNewTodo(newname)

    inputname.value = ""

    postTodo(newname)

    var getUrl = "verif_compte/"

    fetch(getUrl).then(function(response) {
        return response.json()
    }).then(function(data) {
        var verif_compte = data.verif_compte

        for(let utilisateur of verif_compte) {
            displayNewTodo(utilisateur)
        }
    })
}

*/
function postTodo(text) {
   var postUrl = "add-todo"

    fetch(postUrl, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            text: text
        })
    }).then(function(response) {
        return response.json()
    }).then(function(data) {
        console.log("worked")
    })
}

function fetchTodos() {
    var getUrl = "todos/"

    fetch(getUrl).then(function(response) {
        return response.json()
    }).then(function(data) {
        var todos = data.todos

        for(let todo of todos) {
            displayNewTodo(todo)
        }
    })
}




function displayNewTable(text) {
    var tableContainer = document.getElementById("table-container")

    var newTableElement = document.createElement("div")

    newTableElement.innerHTML = text;

    tableContainer.appendChild(newTableElement);
}

function fetchTodos() {
    var getUrl = "uneTable/"

    fetch(getUrl).then(function(response) {
        return response.json()
    }).then(function(data) {

        var maTable = data.uneTable

        for(let table of maTable) {
            displayNewTable(table)
        }
    })
}
