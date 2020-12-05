var email = document.getElementById("email")
var email_div = document.getElementById("emailDiv")
var password2 = document.getElementsByName("password2")[0]
var password2_div = document.getElementById("passwordDiv2");

password2.addEventListener("keyup", function (e){
    if(e.target.value != ""){
        password2_div.className = "login-div password-icon icon-color"
        password2.style.borderBottomColor = "rgba(190,81,184,1)"
    }
    
    else{
        password2.style = "";
        password2_div.className = "login-div password-icon";
    }
});

email.addEventListener("keyup", function (e){
    if(e.target.value != ""){
        email_div.className = "login-div email-icon icon-color"
        email.style.borderBottomColor = "rgba(190,81,184,1)"
    }
    
    else{
        email.style = "";
        email_div.className = "login-div email-icon";
    }
});


