/* Project specific Javascript goes here. */
$(function() {
    FastClick.attach(document.body);

    var card_position = 0;
    var num_cards = $('.card').length;

    $('#heart-button').on('click', function(e){
        e.preventDefault();

        if (card_position === num_cards-1) {
            $(this).off('click');
            return;
        }

        $current_card = $('#card-' + card_position);
        if (Math.random() < 0.5) {
            $current_card.transition({
                                        opacity: 0,
                                        x: 300,
                                        y: -250,
                                        rotate: '40deg',
                                    }, 1400, 'easeOutQuint');
        } else {
            $current_card.transition({
                                        opacity: 0,
                                        x: -300,
                                        y: -250,
                                        rotate: '-40deg',
                                    }, 1400, 'easeOutQuint');
        }

        card_position += 1;
        $('#marker').transition({
                        width: card_position / (num_cards-1) * 100 + "%"
                    }, 700);
    });

});
