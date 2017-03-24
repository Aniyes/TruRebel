/**
 * Created by DreamchaserJunior on 3/22/2017.
 */
var onRight = false;
var onLeft  = true;
randomize = Math.random() * 300;
var square = $('#square');
display = $('#display').append(square.css('margin-left'));

$('#move').on('click',function () {
 //   $(this).animate({

        if( onRight === false){


            square.css('margin-left',Math.random() * 300);

            console.log('Right');
/*
            if (square.css('margin-left') >= 0 && square.css('margin-left') <= 250){

                square.css('background-color','blue');

            if (square.css('margin-left') >= 251 && square.css('margin-left') <= 500){

                square.css('background-color','green');
                console.log('green');

            if (square.css('margin-left') >= 501 && square.css('margin-left') <= 750){

                square.css('background-color','red');
            }
                }
            }
*/
            $('#display').empty();

            $('#display').append(square.css('margin-left'));

            onRight = true;
            onLeft = false;

            
        }else{


            square.css('margin-left',Math.random() * 300);

            console.log('Left');
/*
            if (square.css('margin-left') >= 0 && square.css('margin-left') <= 250){

                square.css('background-color','blue');

            if (square.css('margin-left') >= 251 && square.css('margin-left') <= 500){

                square.css('background-color','green');

            if (square.css('margin-left') >= 501 && square.css('margin-left') <= 750){

                square.css('background-color','red');
            }
                }
            }
*/
            $('#display').empty();

            $('#display').append(square.css('margin-left'));
            onRight = false;
            onLeft = true;

    }

    });

