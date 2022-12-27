formColumn = document.querySelector('#form-column')
formColumn.addEventListener('submit', function (event) {
    event.preventDefault()
})

formCard = document.querySelector('#form-card')
if (formCard != null) {
    formCard.addEventListener('submit', function (event) {
        event.preventDefault()
    })
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
            input = document.querySelector('#create-card')
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

