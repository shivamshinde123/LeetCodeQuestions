/**
 * @param {Object|Array} obj
 * @return {boolean}
 */
var isEmpty = function(obj) {
    // approach 1
    // for (let key in obj){
    //     return false
    // }
    // return true

    // appraoch 2
    return !Object.keys(obj).length
};