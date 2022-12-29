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



function formCard(event){
    event.preventDefault()
}


async function doFetchToAPI(url, body) {
    csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
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
        console.log(data)
    }
}

function createColumn(id) {
    let url = `/api/create-column/${id}`
    const input = document.querySelector('#create-column')
    //title = input.value
    csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
    input.addEventListener('keyup', function (e) {
        if (e.keyCode == 13 && this.value != "") {
            body = JSON.stringify({ 'title': this.value, 'board_id': id })
            doFetchToAPI(url, body)
            this.value = "";
        }
    })
}

function createCard(id) {
    url = `/api/create-card/${id}`
    input = document.querySelector(`#create-card_${id}`)
    // title = input.value
    csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
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
    csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
    const response = await fetch(url, {
        method: 'POST',
        body: json,
        headers: {
            'X-CSRFToken': csrftoken,
            'Content-Type': 'application/json'
        },
    })

}