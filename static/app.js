
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

function reaction(){
    var tableContainer = document.getElementById("oneTable-container")

    var newTableElement = document.createElement("div")

    newTableElement.innerHTML = 'SA fonctionne vraiment WOW such skills  such power woaw!!'

    tableContainer.appendChild(newTableElement)
}

function displayNewTable(text,id) {
    var tableContainer = document.getElementById("table-container")

    var newTableElement = document.createElement("div")

    newTableElement.innerHTML = text
    newTableElement.id = id
    newTableElement.onclick = function (){
        newTableElement.style.color = "red"
        document.getElementById("oneTable-container").appendChild(newTableElement)
    }
    tableContainer.appendChild(newTableElement)

}


function fetchTable() {
    var getUrl = "/tableMagasin/"

    fetch(getUrl).then(function(response) {
        return response.json()
    }).then(function(data) {
        var tableMagasin = data.VectorMagasin

        for(let maTable of tableMagasin) {
            displayNewTable(maTable,maTable[0])
        }
    })
}





