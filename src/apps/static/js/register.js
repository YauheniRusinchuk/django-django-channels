$(function(){


    $('.form_register').on('submit', (e)=> {
        e.preventDefault();
        let login = $('.register_login').val();
        let password = $('.register_password').val();
        let password2 = $('.register_password_confirm').val();

        if(!login) {
            $('.login_error').slideDown('fast');
        }

        if(password.length < 8) {
            $('.login_error_length').slideDown('fast');
        }else if (password !== password2) {
            $('.login_error_confirm').slideDown('fast');
        }

        if(login && password && password2) {
            $.ajax({
                url: $(this).attr('action'),
                type: 'POST',
                data: {
                    username: login,
                    password: password,
                    csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()
                },
                success: function() {
                     window.location.href = "/"
                },

                error: function(){
                    console.log("ERROR")
                }
            })
        }

    })


})
