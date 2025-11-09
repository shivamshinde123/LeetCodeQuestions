/**
 * @param {number[]} nums
 * @return {number[]}
 */
var rearrangeArray = function(nums) {
    
    let pos = new Array()
    let neg = new Array()

    for (let i = 0; i < nums.length; i++){
        if (nums[i] > 0){
            pos.push(nums[i])
        }
        else{
            neg.push(nums[i])
        }
    }

    let ans = new Array()

    for (let i = 0; i < pos.length; i++){
        ans.push(pos[i])
        ans.push(neg[i])
    }

    return ans
};