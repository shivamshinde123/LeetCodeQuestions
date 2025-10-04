/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    
    let n = nums.length;
    let j = -1;

    for (let i = 0; i< n; i++){
        if (nums[i] === 0){
            j = i
            break
        }
    }

    if (j === -1){
        return nums
    }

    for (let i = j + 1; i < n; i++){
        if (nums[i] != 0){
            temp = nums[j]
            nums[j] = nums[i]
            nums[i] = temp
            j += 1
        }
    }

    return nums

};