
$(document).ready(function(){
    console.log("loaded");
    $.material.init();

    $(document).on("submit", "#register-form", function(e){
        e.preventDefault();
        var form = $('#register-form').serialize();
        $.ajax({
            url: '/postregistration',
            type: 'POST',
            data: form,
            success: function(response){
                console.log(response);
            }
        })
    })

    $(document).on("login", "#login-form", function(e){
        e.preventDefault();
        var form = $('check-login').serialize();
        $.ajax({
            url: '/check-login',
            type: 'POST',
            data: form,
            success: function(response){
                if (response == 'error'){
                    alert("Could not log in.");
                }else{
                    console.log("Logged in as," response);
                }
            }
        })
    })
})
