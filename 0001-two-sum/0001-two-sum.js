/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {

    // Brute force approach
    // let n = nums.length;
    // let indices = [];
    // for (let i=0;i<n;i++){
    //     for (let j=i+1;j<n;j++){
    //         if (nums[i] + nums[j] == target){
    //             indices.push(i);
    //             indices.push(j);
    //         }
    //     }
    // }

    // return indices

    // hashmap (value -> index)
    let hashmap = new Map();

    for (let i = 0; i< nums.length; i++){
        let diff = target - nums[i]

        if (hashmap.has(diff)){
           return [hashmap.get(diff), i]
        }

       hashmap.set(nums[i], i)
    }
};