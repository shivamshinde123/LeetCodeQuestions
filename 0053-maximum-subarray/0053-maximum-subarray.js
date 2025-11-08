/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    
    let max = Number.NEGATIVE_INFINITY
    let sum = 0

    for (let i = 0; i < nums.length; i++){

        sum += nums[i]

        if (sum > max){
            max = sum
        }

        if (sum < 0){
            sum = 0
        }

        // To consider the sum of the empty subarray
        // uncomment the following check

        // if (max < 0) {
        //     max = 0
        // }
    }

    return max
};