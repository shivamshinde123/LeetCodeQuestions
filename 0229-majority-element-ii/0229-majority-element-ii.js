/**
 * @param {number[]} nums
 * @return {number[]}
 */
var majorityElement = function(nums) {
    
    threshold = Math.floor(nums.length/3)
    let req_freq = {}
    
    for (let num of nums){
        if (num in req_freq){
            req_freq[num] += 1
        }
        else{
            req_freq[num] = 1
        }
    }
    
    let answer = []
    for (let key of Object.keys(req_freq)){
        if (req_freq[key] > threshold){
            answer.push(key)
        }
    }
    
    return answer
};