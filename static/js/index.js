
async function createColumn(id) {
    value = document.getElementById('#create-column').value
    if (value != "") {
        value.submit()
        await fetch('create-column', {
            method: 'POST',
            body: { 'value': value,'id':id },
            headers: {
                'X-CSRFToken': csrftoken,
            },
        })
    value = ""
    }
}