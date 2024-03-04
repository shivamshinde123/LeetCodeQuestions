/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumGap = function(nums) {
    
    nums.sort((a,b) => {
        if (a<b){
            return -1
        }
        else if (a>b){
            return 1
        }
        else{
            return 0
        }
    })
    
    let max_diff = 0
    
    for (let i = 0; i < nums.length - 1; i++){
        let local_diff = Math.abs(nums[i] - nums[i+1])
         
        if (local_diff > max_diff){
            max_diff = local_diff
        }
    }
    
    return max_diff
};