/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function (functions) {

    return function (x) {
        if (functions.length === 0){
            return x
        }
        input = x
        output = null
        for (let i = functions.length - 1; i >= 0; i--) {
            output = functions[i](input)
            input = output
        }
        return output
    }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */