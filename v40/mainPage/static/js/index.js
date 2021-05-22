function showDivPassive() {
    document.getElementById('active_div').style.display = "none";
    document.getElementById('passive_div').style.display = "block";
    document.getElementById('passive_div').scrollIntoView();
}
function showDivActive() {
    document.getElementById('passive_div').style.display = "none";
    document.getElementById('active_div').style.display = "block";
    document.getElementById('active_div').scrollIntoView();
}




function showDivSignin() {
    document.getElementById('signup').style.display = "none";
    document.getElementById('active_div').style.display = "none";
    document.getElementById('passive_div').style.display = "none";
    document.getElementById('signin').style.display = "block";
    
}

function showDivSignup() {
    document.getElementById('signin').style.display = "none";
    document.getElementById('signup').style.display = "block";
    
}

function confirmEmail() {
    var email = document.getElementById("my_email").value
    var confemail = document.getElementById("retype_email").value
    if(email != confemail) {
        alert('Email Not Matching!');
    }
}





