/*!
 * \brief fonction permettant d importer de la base de donnees
 * \fn string function fetchTodos()
 * \return string replaced string
 */
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

/*!
 * \brief fonction permettant de mettre a jour la page achat
 * \fn string function reaction()
 * \return string dans id oneTable-container
 */
function reaction(){
    var tableContainer = document.getElementById("oneTable-container")

    var newTableElement = document.createElement("div")

    newTableElement.innerHTML = sessionStorage.getItem("beerChoice")

    tableContainer.appendChild(newTableElement)
}

/*!
 * \brief fonction imprime les donnees dans le magasin
 * \fn string function displayNewTable(text,id)
 * \param in text une chaine de string de la description de la biere
 * \param in id un string contenant id de la biere
 * \return string donnees de biere dans table-container
 */
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

/*!
 * \brief fonction permettant d importer de la base de donnees les donnees du magasin
 * \fn string function fetchTable()
 * \return string des donnees de la biere pour le magasin
 */
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

/*!
 * \brief fonction permettant de stocker les donnes dans le panier du client
 * \fn string function postAchat(beer_id,username,quantity)
 * \param in beer_id le id de la biere
 * \param in username le username du client
 * \param in quantity la quantite choisit a commander
 */
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

/*!
 * \brief fonction permettant de prendre les donnees du html a la fonction post achat
 * quand laction du click est utilisee
 * \fn string ronButtonAchat()
 * \return postAchat une demande de stockage au server
 */
function onButtonAchat() {
    var inputElement = document.getElementById("quantity")

    var newTodoText = inputElement.value

    inputElement.value = ""

    postAchat(sessionStorage.getItem("beerId"),
        sessionStorage.getItem("pseudo_user"),
        newTodoText)
}

/*!
 * \brief fonction permettant de confirmer un utilisateur
 * \fn string replaceStrings(translation, parameters)
 * \param in username le nom de l utilisateur
 * \param in le password de l utilisateur
 */
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

/*!
 * \brief fonction permettant d afficher le nom de l utilisateur
 * POURRAIS ETRE AMELIORER EN PASSANT PAR URL
 * \fn string onClickLogin()
 * \return objet display user qui permet d afficher un user
 */
function onClickLogin() {

    var userContainer = document.getElementById("pseudo_user")
    var passwordContainer = document.getElementById("password")

    sessionStorage.setItem("pseudo_user", userContainer.value)
    sessionStorage.setItem("password", passwordContainer.value)

    postUser(sessionStorage.getItem("pseudo_user"),sessionStorage.getItem("password"))
    displayUser()
}

/*!
 * \brief fonction permettant d afficher le user sur tous les pages html
 * \fn string displayUser()
 * \return string contenue dans le conteneur user-container
 */
function displayUser() {
    var userContainer = document.getElementById("user-container")

    var newTableElement = document.createElement("div")

    newTableElement.innerHTML = sessionStorage.getItem("pseudo_user")
    userContainer.innerHTML=""
    userContainer.appendChild(newTableElement)
}

/*!
 * \brief fonction permettant d importer de la base de donnees les biere par categories
 * \fn string fetchTodoWithQuery(query)
 * \param in query le type de biere ipa rousse blonde etc.
 * \return une fonction displayNewTable qui affiche les donnees du query
 */
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

/*!
 * \brief fonction permettant un tries selon la category choisit ipa, rousse, blonde etc.
 * \fn string select_type(clicked_id)
 * \param in l ID de lobjet clicker
 * \return un query de la demande pour le type de biere choisit
 */
function select_type(clicked_id) {
    var inputElement = document.getElementById(clicked_id)

    var search = inputElement.value
    var tableContainer = document.getElementById("table-container")
    tableContainer.innerHTML=""
    fetchTodoWithQuery(search)
}

/*!
 * \brief fonction permettant d afficher les commandes du client
 * \fn string fetchCommandeWithQuery()
 * \return string des commandes
 */
function fetchCommandeWithQuery() {
    var getUrl = "/panier_commande/"

    fetch(getUrl).then(function(response) {
        return response.json()
    }).then(function(data) {
        todos = data.todos

        for (let todo of todos) {
            displayNewPanier(todo)
        }
    })
}

/*!
 * \brief fonction permettant d afficher les donnees du client dans le panier
 * \fn string displayNewPanier(text)
 * \param in text les differentes commande du client
 * \return string replaced string
 */
function displayNewPanier(text) {
    var tableContainer = document.getElementById("panier-commande")
    var newTableElement = document.createElement("div")

    newTableElement.innerHTML=text
    newTableElement.accessKey=text
    newTableElement.textContent=text
    newTableElement.id=text
    newTableElement.value=text
    newTableElement.innerHTML=text
    newTableElement.accessKey=text
    newTableElement.textContent=text
    newTableElement.id=text
    newTableElement.value=text

    tableContainer.appendChild(newTableElement)
}

