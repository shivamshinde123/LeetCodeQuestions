/**
 * @param {number[]} nums
 * @return {number}
 */
var largestPerimeter = function(nums) {
    let maxP = 0
    let n = nums.length
    
    if (n < 3){
        return -1
    }
    
    nums.sort((a,b)=>b-a)
    
    
    let arr_sum = (arr) => {
        let sum_of_elems = arr.reduce((accumulator, current_val) => {
            return accumulator + current_val
        }, 0)
        return sum_of_elems
    }
    
    let i = 0
    while (i < n-2){
        if (nums[i] < arr_sum(nums.slice(begin=i+1))){
            maxP = Math.max(maxP, arr_sum(nums.slice(begin=i)))
            break
        }
        i = i + 1
    }
    
    if (maxP === 0){
        return -1
    }
    return maxP
};