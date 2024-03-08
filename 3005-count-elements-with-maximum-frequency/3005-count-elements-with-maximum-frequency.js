/**
 * @param {number[]} nums
 * @return {number}
 */
var maxFrequencyElements = function(nums) {
    
    let freq = {}
    
    for (let num of nums){
        if (num in freq){
            freq[num] += 1
        }
        else {
            freq[num] = 1
        }
    }
    
    /*
    The "..." syntax in JavaScript is called the spread syntax or spread operator. It allows an iterable (such as an array) to be expanded into individual elements. It is commonly used for concatenating arrays, passing arguments to functions, or copying array or object properties.
    */
    
    let max_freq = Math.max(...Object.values(freq))

    let total_freq = 0
    for (let value of Object.values(freq)){
        if (value === max_freq){
            total_freq += value
        }
    }
    
    return total_freq
};