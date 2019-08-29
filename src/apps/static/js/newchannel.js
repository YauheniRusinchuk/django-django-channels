$(function(){


    $('.form_new_channel').on('submit', (e)=> {
        e.preventDefault();
        let name = $('.newchannel_name').val();
        let password = $('.newchannel_password').val();

        if (!name) {
            $(".name_error").slideDown('fast');
        }

        if(name) {
            $.ajax({
                url: $(this).attr('action'),
                type: 'POST',
                data: {
                    name: name,
                    password: password,
                    csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()
                },
                success: function() {
                    $('.check_good').slideDown('fast');
                    setTimeout(function(){
                        window.location.href = "/"
                    }, 1000)
                },
                error: function() {
                    console.log('error');
                }
            })
        }
    })
})
