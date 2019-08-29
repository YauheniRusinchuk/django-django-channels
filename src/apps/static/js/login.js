$(function(){
    $('.form_login').on('submit', (e)=> {
        e.preventDefault();
        let login = $('.login_input').val();
        let password = $('.password_input').val();


        if(login && password) {
             $.ajax({
                 url: $(this).attr('action'),
                 type: 'POST',
                 data: {
                     username: login,
                     password: password,
                     csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()

                 },
                 success: function() {
                     $('.login_checked').slideDown('fast', ()=> {
                         setTimeout(function(){
                             window.location.href = "/"
                         }, 1000)
                     })
                 },

                 error: function(){
                     $('.login_error').slideDown('fast', ()=> {
                         setTimeout(function(){
                              $('.login_error').slideUp('fast');
                         }, 1000)
                     })
                 }
            })
        }
    })
})
