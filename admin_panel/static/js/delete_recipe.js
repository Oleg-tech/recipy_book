$(document).ready(function(){
    $(".delete-form").submit(function(e){
        e.preventDefault()
        const post_id = $(this).attr('id')
        console.log(post_id)

        $.ajax({
            type:'POST',
            url: '/delete-recipe',
            dataType: 'json',
            data: {
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
                'post_id': post_id,
            },
            success: function(){
                console.log();
                $("#"+post_id).remove();
            },
            error: function(response){
                console.log('error');
            }
        });
    });
});