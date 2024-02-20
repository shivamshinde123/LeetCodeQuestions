/**
 * @param {string} moves
 * @return {boolean}
 */
var judgeCircle = function(moves) {
    let x = 0
    let y = 0
    
    for (let move of moves){
        if (move === 'R'){
            x += 1
        }
        else if (move === 'L'){
            x -= 1
        }
        else if (move === 'U'){
            y += 1
        }
        else {
            y -= 1
        }
    }
    
    return x === 0 && y === 0
};