
function onButtonClick() {
    var inputname = document.getElementById("pseudo_user")

    var newname = inputname.value

    displayNewTodo(newname)

    inputname.value = ""

    postTodo(newname)
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



/*
function displayNewTable(text) {
    var tableContainer = document.getElementById("table-container")

    var newTableElement = document.createElement("div")

    newTableElement.innerHTML = text;

    tableContainer.appendChild(newTableElement);
}
*/

function fetchTable() {
    var getUrl = "/uneTable/"

    fetch(getUrl).then(function(response) {
        return response.json()
    }).then(function(data) {

        var maTable = data.xtable

        for(let table of maTable) {
            displayNewTable(table)
        }
    })
}

