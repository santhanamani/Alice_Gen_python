


function datasend() {

    fetch("/datasend", {
        method: "POST",
        body : JSON.stringify({
        "id" : document.getElementById('id').value,
        "name" : document.getElementById('name').value,
        "state" : document.getElementById('state').value,
        })
    }).then(
        response => response.text() // .json(), etc.
        // same as function(response) {return response.text();}
    ).then(
        html => {
            console.log(html);
            alert("data send successfully");
        }
    );
}


function dataget() {

    fetch("/dataget", {
        method: "GET",
    }).then(
        response => response.text() // .json(), etc.
        // same as function(response) {return response.text();}
    ).then(
        html => {
            console.log(html)
            document.getElementById("textareaid").value = html;
        }
    );
}