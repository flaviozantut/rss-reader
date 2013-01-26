jQuery(document).ready(function($) {
    /**
     * Slider de noticias
     */
    var width = $('.rss-news li:first')
        .addClass('active')
        .width();
    $('#rss-prev').addClass('stop');
    $('.rss-news li').each(function(i, val){
        $(this).css('left', (i)*width);
    });
    $('.rss-news li').css('display', 'block');
    $('#rss-next').click(function(){
        if( !$('.rss-news li:last').hasClass('active') ){
            $('.rss-news .active').removeClass('active').next().addClass('active');
            $('.rss-news li').each(function(i, val){
                $(this).stop(true, true).animate({'left': (parseInt($(this).css('left')))-width},500);
            });
            $(this).removeClass('stop');
            $('#rss-prev').removeClass('stop');
        }else{
            $(this).addClass('stop');

        }
    });
    $('#rss-prev').click(function(){
        if( !$('.rss-news li:first').hasClass('active') ){
            $('.rss-news .active').removeClass('active').prev().addClass('active');
            $('.rss-news li').each(function(i, val){
                $(this).stop(true, true).animate({'left': (parseInt($(this).css('left')))+width},500);
            });
            $(this).removeClass('stop');
            $('#rss-next').removeClass('stop');
        }else{
            $(this).addClass('stop');
        }
    });
    /**
     * Modal
     */
    $('.rss-news a').click(function(e){
        e.preventDefault();
        title = '<h1 class="title">' + $(this).html() + '</h1>';
        orig = '<a href="'+$(this).attr('href')+'"> ler artigo original </a>';
        content = '<article>'+$(this).next().clone().html()+ '</article>';
        $('body').append(
            '<div class="modal" style="display:none"><div class="content"><div class="close">Fechar</div>'+
            title +
            content +
            '<br />'+
            orig +
            '</div></div>'
        );
        $('.modal').fadeIn('fast');
    });
    $(document).on("click", ".close", function(e){

       $('.modal').fadeOut('fast', function(){
        $(this).remove();
       });
    });


});