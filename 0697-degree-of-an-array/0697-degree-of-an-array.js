/**
 * @param {number[]} nums
 * @return {number}
 */
var findShortestSubArray = function(nums) {
    let first_occurence_index = {}
    let freq = {}
    let result = 0
    let degree = 0
    
    for (let [index, element] of nums.entries()){
        if (!(element in first_occurence_index)){
            first_occurence_index[element] = index
        }
        
        if (element in freq){
            freq[element] += 1
        }
        else{
            freq[element] = 1
        }
        
        if (freq[element] > degree){
            degree = freq[element]
            result = index - first_occurence_index[element] + 1
        }
        else if (freq[element] === degree){
            result = Math.min(result, index - first_occurence_index[element] + 1)
        }
        
    }
    
    
    
    return result
};