/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    
    let n = nums.length
    let left_index = 0
    let right_index = n - 1
    
    while (left_index <= right_index){
        
        let mid_index = left_index + Math.floor((right_index - left_index) / 2)
        let mid_value = nums[mid_index]
        
        if (mid_value == target){
            return mid_index
        }
        else if (mid_value > target){
            right_index = mid_index - 1
        }
        else {
            left_index = mid_index + 1
        }
    }
    
    return right_index + 1
};