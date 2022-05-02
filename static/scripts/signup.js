const firstNameInput = document.getElementById("firstName");
const lastNameInput = document.getElementById("lastName");
const emailInput = document.getElementById("email");
const usernameInput = document.getElementById("username");
const passwordInput = document.getElementById("password");

document.getElementById("signup-form").onsubmit = function (event) {
    event.preventDefault();
    const firstName = firstNameInput.value;
    const lastName = lastNameInput.value;
    const email = emailInput.value;
    const username = usernameInput.value;
    const password = passwordInput.value;
    fetch("/signup", {
        method: "POST",
        body: JSON.stringify({
            "firstName": firstName,
            "lastName": lastName,
            "email": email,
            "username": username,
            "password": password
        }),
        headers: {
            "Content-Type": "application/json"
        }
    }).then(function(response) {


    })
}