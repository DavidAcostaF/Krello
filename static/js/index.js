
formColumn = document.querySelector('#form-column')
formColumn.addEventListener('submit', function (event) {
    event.preventDefault()
})

formCard = document.querySelector('#form-card')
formCard.addEventListener('submit', function (event) {
    event.preventDefault()
})


async function doFetchToAPI(url, body) {
    csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
    if (body.title != "") {
        await fetch(url, {
            method: 'POST',
            body: body,
            headers: {
                'X-CSRFToken': csrftoken,
                'Content-Type': 'application/json'
            },
        })
    }
}

function createColumn(id) {
    url = `/api/create-column/${id}`
    input = document.querySelector('#create-column')
    title = input.value
    csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
    body = JSON.stringify({ 'title': title, 'board_id': id })
    input.addEventListener('keyup', async function (event) {
        if (event.code === 'Enter') {
            doFetchToAPI(url, body)
            input.value = ""
        }
    })
}

function createCard(id) {
    url = `/api/create-card/${id}`
    input = document.querySelector('#create-card')
    title = input.value
    csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
    body = JSON.stringify({ 'title': title, 'column_id': id })
    input.addEventListener('keyup', async function (event) {
        if (event.code === 'Enter') {
            doFetchToAPI(url, body)
            input.value = ""
        }
})
}

