$(function(){

    $('.checkpassword_form').on('submit', (e)=> {
        e.preventDefault();

        let password = $('.password_check').val();

        if (!password) {
            $('.password_required').slideDown('fast');
        }

        if(password) {
            $.ajax({
                url: $(this).attr('action'),
                type: 'POST',
                data: {
                    password: password,
                    csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()
                },
                success: function() {
                    console.log("GOOOD")
                },
                error: function() {
                    console.log("ERROR")
                }
            })
        }
    })
})
