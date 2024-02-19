/**
 * @param {number[]} nums
 * @return {boolean}
 */
var isMonotonic = function(nums) {
    
    if (nums[nums.length-1] > nums[0]){
        for (let i = 0; i < nums.length-1;i++){
            if (nums[i+1] - nums[i] < 0){
                return false
            }
        }
    }
    else{
        for (let i = 0; i < nums.length-1;i++){
            if (nums[i+1] - nums[i] > 0){
                return false
            }
        }
    }
    
    return true
};