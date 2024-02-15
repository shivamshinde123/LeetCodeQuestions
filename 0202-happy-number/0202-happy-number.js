/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function(n) {
    let seen = new Set()

    let sq_sum_of_digits = (n) => {
        let sq_sum = 0
        while (n !== 0){
            let digit = n % 10
            sq_sum += digit**2
            n = Math.floor(n/10)
        }
        return sq_sum
    }

    while (true){
        sq_sum = sq_sum_of_digits(n)
        if (sq_sum === 1){
            return true
        }
        else if (seen.has(sq_sum)){
            return false
        }

        seen.add(sq_sum)
        n = sq_sum
    }
};