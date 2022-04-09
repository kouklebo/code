
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
        sessionStorage.getItem("pseudo_user"),
        newTodoText)
}


function postUser(username,password) {
   var postUrl = "/compte_verif/"

    fetch(postUrl, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            username: username,
            password: password
        })
    }).then(function(response) {
        return response.json()
    }).then(function(data) {
        console.log("worked")
    })
}


function onClickLogin() {

    var userContainer = document.getElementById("pseudo_user")
    var passwordContainer = document.getElementById("password")

    sessionStorage.setItem("pseudo_user", userContainer.value)
    sessionStorage.setItem("password", passwordContainer.value)

    postUser(sessionStorage.getItem("pseudo_user"),sessionStorage.getItem("password"))
    displayUser()
}


function displayUser() {
    var userContainer = document.getElementById("user-container")

    var newTableElement = document.createElement("div")

    newTableElement.innerHTML = sessionStorage.getItem("pseudo_user")
    userContainer.innerHTML=""
    userContainer.appendChild(newTableElement)
}


function selectType() {
    sessionStorage.setItem("beerChoice", tableContainer.accessKey)
    sessionStorage.setItem("beerId", tableContainer.id)
    sessionStorage.setItem("pseudo_user", userContainer.value)
    sessionStorage.setItem("password", passwordContainer.value)
}


function fetchTodoWithQuery(query) {
    var getUrl = "/magasin/style/?query=" + query

    fetch(getUrl).then(function(response) {
        return response.json()
    }).then(function(data) {
        todos = data.todos

        for (let todo of todos) {
            displayNewTable(todo, todo[0])
        }
    })
}


function select_type(clicked_id) {
    var inputElement = document.getElementById(clicked_id)

    var search = inputElement.value
    var tableContainer = document.getElementById("table-container")
    tableContainer.innerHTML=""
    fetchTodoWithQuery(search)
}


function fetchCommandeWithQuery() {
    var getUrl = "/panier_commande/?user=" + sessionStorage.getItem("pseudo_user")

    fetch(getUrl).then(function(response) {
        return response.json()
    }).then(function(data) {
        todos = data.todos

        for (let todo of todos) {
            displayNewPanier(todo)
        }
    })
}


function displayNewPanier(text="patate") {
    var tableContainer = document.getElementById("panier-commande")
    var newTableElement = document.createElement("div")

    newTableElement.innerText=text

    tableContainer.appendChild(newTableElement)
}

