/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumClosest = function(nums, target) {
    
    let n = nums.length 
    diff = Infinity
    answer = 0
    
    let compareFn = (a,b) => {
        if (a < b){
            return -1
        }
        else if (a > b) {
            return 1
        }
        else{
            return 0
        }
    }
    
    nums.sort(compareFn)
    
    for (let i = 0; i < n - 1; i++){
        let j = i + 1
        let k = n - 1
        
        while (j < k){
            let sum_ = nums[i] + nums[j] + nums[k]
            
            local_diff = Math.abs(sum_ - target)
            
            if (local_diff < diff){
                diff = local_diff
                answer = sum_
            }
            
            if (sum_ < target) {
                j += 1
            }
            else if (sum_ > target){
                k -= 1
            }
            else {
                j += 1
            }
        }
    }
    
    return answer
    
    
};