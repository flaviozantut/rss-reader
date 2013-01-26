jQuery(document).ready(function($) {
    //alert('teste');
    var width = $('.rss-news li:first')
        .addClass('active')
        .width();
    $('#rss-prev').addClass('stop');
    $('.rss-news li').each(function(i, val){
        $(this).css('left', (i)*width);
    });
    $('#rss-next').click(function(){
        if( !$('.rss-news li:last').hasClass('active') ){
            $('.rss-news .active').removeClass('active').next().addClass('active');
            $('.rss-news li').each(function(i, val){
                $(this).css('left', (parseInt($(this).css('left')))-width);
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
                $(this).css('left', (parseInt($(this).css('left')))+width);
            });
            $(this).removeClass('stop');
            $('#rss-next').removeClass('stop');
        }else{
            $(this).addClass('stop');
        }
    });
});