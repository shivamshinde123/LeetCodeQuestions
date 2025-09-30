/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k) {
    n = nums.length
    k = k % n
    temp = nums.slice(n-k, n)

    for (let i = n-k-1; i>-1; i--){
        nums[i+k] = nums[i]
        
    }

    for (let i=0;i<k;i++){
        nums[i] = temp[i]
    }
};