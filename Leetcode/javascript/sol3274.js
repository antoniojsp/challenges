/**
 * @param {string} coordinate1
 * @param {string} coordinate2
 * @return {boolean}
 */
var checkTwoChessboards = function(coordinate1, coordinate2) {
    /* Imagine that each square has a value made from adding the coordinates. i.e. a = 1
    b = 2, c = 3, etc. Then a1 = 1 + 1 = 2. a6 = 1 = 6 = 7, etc
    If the result of this ooperation is even, then is black, odd is white.
    we check that both coordinates are the same color using this logic*/

    function get_square_value(pos){
        values = {"a":1,"b":2, "c":3,"d":4,"e":5,"f":6,"g":7,"h":8}
        return  parseInt(pos[1]) + values[pos[0]]
    }

    odd_or_even = (num) =>  num % 2 == 0 ? "even":"odd"

    return odd_or_even(get_square_value(coordinate1)) == odd_or_even(get_square_value(coordinate2));
}