
form = document.querySelector('#form-column')
form.addEventListener('submit', function (event) {
    event.preventDefault()
})

function createColumn(id) {
    input = document.querySelector('#create-column')
    title = input.value
    csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
    input.addEventListener('keyup', async function (event) {
        if (event.code === 'Enter') {
            if (title != "") {
                await fetch(`/api/create-column/${id}`, {
                    method: 'POST',
                    body: JSON.stringify({'title': title, 'board_id': id}),
                    headers: {
                        'X-CSRFToken': csrftoken,
                        'Content-Type': 'application/json'
                    },
                })
                input.value = ""
            }
        }
    })
}
