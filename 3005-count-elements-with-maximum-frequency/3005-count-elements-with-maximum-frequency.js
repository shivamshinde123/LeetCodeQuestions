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
    
    let max_freq = Math.max(...Object.values(freq))

    let total_freq = 0
    for (let value of Object.values(freq)){
        if (value === max_freq){
            total_freq += value
        }
    }
    
    return total_freq
};