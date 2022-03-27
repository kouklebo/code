
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



function displayNewTable(text,id) {
    var tableContainer = document.getElementById("table-container")


    var newTableElement = document.createElement("div",id)

    newTableElement.innerHTML = text

        newTableElement.onclick = function()
        {
            newTableElement.style = "Color: red"

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

function displayNewWindow(){

}




