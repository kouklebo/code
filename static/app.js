
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

    newTableElement.innerHTML = sessionStorage.getItem("beerChoice")

    tableContainer.appendChild(newTableElement)
}


function session(){
    var tableContainer = document.getElementById("oneTable")

    var newTableElement = document.createElement("div")

    newTableElement.innerHTML = sessionStorage.getItem("info_user")

    tableContainer.appendChild(newTableElement)
}


function displayNewTable(text,id) {
    var tableContainer = document.getElementById("table-container")

    var newTableElement = document.createElement("div")

    newTableElement.onclick = function (){
        newTableElement.style.color="red"
        tableContainer.id = id
        tableContainer.accessKey=text
        sessionStorage.setItem("beerChoice", tableContainer.accessKey)
        sessionStorage.setItem("beerId", tableContainer.id)
    }

    newTableElement.innerHTML = text
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


function postAchat(beer_id,username,quantity) {
   var postUrl = "/choixPanier/"

    fetch(postUrl, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            beer_id: beer_id,
            username: username,
            quantity: quantity
        })
    }).then(function(response) {
        return response.json()
    }).then(function(data) {
        console.log("worked")
    })
}


function onButtonAchat() {
    var inputElement = document.getElementById("quantity")

    var newTodoText = inputElement.value

    inputElement.value = ""

    postAchat(sessionStorage.getItem("beerId"),
        "bob",
        newTodoText)
}


function fetchUser() {
    var getUrl = "/compte_login/"

    fetch(getUrl).then(function(response) {
        return response.json()
    }).then(function(data) {
        sessionStorage.setItem("pseudo", tableContainer.accessKey) = data.pseudo_user

        }
    )
}







