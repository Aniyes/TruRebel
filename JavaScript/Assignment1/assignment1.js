/**
 * Created by Anidyes on 3/20/2017.
 */
$(document).ready(function () {

console.log("loaded");


    $("#addButton").on('click', function () {


        var a = $('#numberOne').val();
        var b = $('#numberTwo').val();
        add(a,b);

    });

    $("#subtractButton").on('click', function () {


        var a = $('#numberOne').val();
        var b = $('#numberTwo').val();
        subtract(a,b);

    });

    $("#divideButton").on('click', function () {

        var a = $('#numberOne').val();
        var b = $('#numberTwo').val();
        divide(a,b);

    });

    $("#multiplyButton").on('click', function () {


        var a = $('#numberOne').val();
        var b = $('#numberTwo').val();
        multiply(a,b);

    });

})

function add(a,b) {

    var sum = parseInt(a) + parseInt(b);
    console.log(sum);
}

function subtract(a,b) {

    var difference = parseInt(a) - parseInt(b);
    console.log(difference);
}

function divide(a,b){

    var quotient = parseInt(a) / parseInt(b);
    console.log(quotient)
}

function multiply(a,b){

    var product = parseInt(a) * parseInt(b);
    console.log(product)
}