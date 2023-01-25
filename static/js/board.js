;(function(){
    const modal = new bootstrap.Modal(document.getElementById('modal'))

    htmx.on('htmx:afterSwap',(e)=>{
        if (e.detail.target.id === "dialog")
        modal.show()
    })
    
    htmx.on('htmx:beforeSwap',(e)=>{
        if (e.detail.target.id === "dialog" && !e.detail.xhr.response)
        modal.hide()
    })
})()

formColumn = document.querySelector('#form-column')
formColumn.addEventListener('submit', function (event) {
    event.preventDefault()
})

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

function formCard(event){
    event.preventDefault()
}


async function doFetchToAPI(url, body) {
    if (body.title != "") {
        const response = await fetch(url, {
            method: 'POST',
            body: body,
            headers: {
                'X-CSRFToken': csrftoken,
                'Content-Type': 'application/json'
            },
        })
        const data = await response.json()
        return data
    }
}

function createColumn(id) {
    let url = `/api/create-column/${id}`
    const input = document.querySelector('#create-column')
    const listContainer = document.querySelector('#lists-container')
    //title = input.value
    input.addEventListener('keyup', function (e) {
        if (e.keyCode == 13 && this.value != "") {
            body = JSON.stringify({ 'title': this.value, 'board_id': id })
            const response = doFetchToAPI(url, body)
            this.value = "";
            listContainer.innerHTML =+ `div class="list">
            <h3 class="list-title">${response.title}</h3>
            <ul class="list-items" id="list-items_${response.id}" ondrop="dropIt(event,${response.id})" ondragover="allowDrop(event)">
            </ul>
            <form id="form-card" onsubmit="event.preventDefault()">
                <input type="text" id="create-card_${response.id}" onchange="createCard(${response.id})"
                    class="add-card-btn boton create-card" placeholder="Add a card">
            </form>
        </div>`;
        }
    })
}

function createCard(id) {
    url = `/api/create-card/${id}`
    input = document.querySelector(`#create-card_${id}`)
    console.log(input)
    input.addEventListener('keyup', async function (e) {
        if (e.keyCode == 13 && this.value != "") {
            body = JSON.stringify({ 'title': this.value, 'column_id': id })
            doFetchToAPI(url, body)
            this.value = ""
        }
    })
}

function allowDrop(ev) {
    ev.preventDefault();  // default is not to allow drop
}

function dragStart(ev,card_id) {
    // The 'text/plain' is referring the Data Type (DOMString) 
    // of the Object being dragged.
    // ev.target.id is the id of the Object being dragged
    ev.dataTransfer.setData("text/plain", ev.target.id);
    let values = {
        "card_id":card_id,
    }

    ev.dataTransfer.setData("text/json", JSON.stringify(values));
}

function dropIt(ev,column_id) {
    ev.preventDefault();  // default is not to allow drop
    let jsonString = ev.dataTransfer.getData("text/json");
    let json = JSON.parse(jsonString);
    let sourceId = ev.dataTransfer.getData("text/plain");
    let sourceIdEl = document.getElementById(sourceId);
    let sourceIdParentEl = sourceIdEl.parentElement;
    // ev.target.id here is the id of target Object of the drop
    let targetEl = document.getElementById(ev.target.id);
    let targetParentEl = targetEl.parentElement;
    let url = `/api/move-card/${json.card_id}`
    let card = sourceIdEl;
    let columnJson = {
        "column_id":column_id,
    }
    // Compare List names to see if we are going between lists
    // or within the same list
    
    // # TODO: parece que esto no funciona porque hay que hacer otro parentElement
    if (targetParentEl.id !== sourceIdParentEl.id) {
        // If the source and destination have the same 
        // className (card), then we risk dropping a Card in to a Card
        // That may be a cool feature, but not for us!
        if (targetEl.className === sourceIdEl.className) {
            // Append to parent Object (list), not to a 
            // Card in the list
            // This is in case you drag and drop a Card on top 
            // of a Card in a different list
            targetParentEl.appendChild(card);
            moveCardFetch(url,JSON.stringify(columnJson))
        } else {
            targetEl.appendChild(card);
            moveCardFetch(url,JSON.stringify(columnJson))
        }
    } else {
        // Same list. Swap the text of the two cards
        // Just like swapping the values in two variables

        // Temporary holder of the destination Object
        let holder = targetEl;
        // The text of the destination Object. 
        // We are really just moving the text, not the Card
        let holderText = holder.textContent;
        // Replace the destination Objects text with the sources text
        targetEl.textContent = sourceIdEl.textContent;
        // Replace the sources text with the original destinations
        sourceIdEl.textContent = holderText;
        holderText = '';
    }
}

async function moveCardFetch(url,json){
    const response = await fetch(url, {
        method: 'POST',
        body: json,
        headers: {
            'X-CSRFToken': csrftoken,
            'Content-Type': 'application/json'
        },
    })
}


async function saveDescriptionCard(card_id){
    let url = `/api/save-description-card/${card_id}`
    let description = document.querySelector(`#description_${card_id}`)
    let body = JSON.stringify({ 'description': description.value })
    if(description.value != ""){
        const response = await fetch(url, {
            method: 'POST',
            body: body,
            headers: {
                'X-CSRFToken': csrftoken,
                'Content-Type': 'application/json'
                },
            })
    }
    //const data = await response.json()
}


async function saveCommentCard(card_id){
    let url = `/api/save-comment-card/${card_id}`
    let activity = document.querySelector(`#comment_${card_id}`)
    let body = JSON.stringify({ 'comment': activity.value })
    if(activity.value != ""){
        const response = await fetch(url, {
            method: 'PATCH',
            body: body,
            headers: {
                'X-CSRFToken': csrftoken,
                'Content-Type': 'application/json'
                },
            })
    }
    //const data = await response.json()
}

async function addBoardToFavorite(board_id){
    let url = `/api/add-board-to-favorite/${board_id}`
    let input = document.querySelector(`#star-${board_id}`)
    console.log(input)
    await fetch(url, {
        method: 'PUT',
        headers: {
            'X-CSRFToken': csrftoken,
            'Content-Type': 'application/json'
            },
        })
        if(input.classList.contains('fa-solid')){
            input.classList.remove('fa-solid')
        }else{
            input.classList.add('fa-solid')
        }
}