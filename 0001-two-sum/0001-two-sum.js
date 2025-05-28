/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let n = nums.length;
    let indices = [];
    for (let i=0;i<n;i++){
        for (let j=i+1;j<n;j++){
            if (nums[i] + nums[j] == target){
                indices.push(i);
                indices.push(j);
            }
        }
    }

    return indices
};