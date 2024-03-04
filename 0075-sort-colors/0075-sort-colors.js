/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function(nums) {
    
    let swap_action = (nums, i, j) => {
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
    }
    
    let l = 0
    let r = nums.length - 1
    let i = 0
    
    while (i <= r){
        if (nums[i] === 0){
            swap_action(nums, i, l)
            i += 1
            l += 1
        }
        else if (nums[i] === 2){
            swap_action(nums, i, r)
            r -= 1
        }
        else{
            i += 1
        }
    }
    
};