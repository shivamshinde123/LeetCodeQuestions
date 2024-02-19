/**
 * @param {number[]} candyType
 * @return {number}
 */
var distributeCandies = function(candyType) {
    let unique_candy_types = new Set(candyType);
    
    
    return Math.min(unique_candy_types.size, Math.floor(candyType.length/2))
};