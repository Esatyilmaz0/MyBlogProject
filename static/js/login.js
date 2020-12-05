var username = document.getElementById("username")
var password = document.getElementById("password");
var username_div = document.getElementById("usernameDiv")
var password_div = document.getElementById("passwordDiv")

username.addEventListener("keyup", function (e){
    if(e.target.value != ""){
        username_div.className = "login-div username-icon icon-color"
        username.style.borderBottomColor = "rgba(190,81,184,1)"
    }
    
    else{
        username.style = "";
        username_div.className = "login-div username-icon";
    }
});

password.addEventListener("keyup", function (e){
    if(e.target.value != ""){
        password_div.className = "login-div password-icon icon-color"
        password.style.borderBottomColor = "rgba(190,81,184,1)"
    }
    else{
        password.style = "";
        password_div.className = "login-div password-icon";
    }
});
