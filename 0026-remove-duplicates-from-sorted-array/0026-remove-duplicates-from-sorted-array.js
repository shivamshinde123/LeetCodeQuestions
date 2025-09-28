/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    let n = nums.length
    let i = 0

    for (let j = 1; j < n; j++){
        if (nums[i] != nums[j]){
            i += 1
            let temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        }
    }

    return i + 1
};