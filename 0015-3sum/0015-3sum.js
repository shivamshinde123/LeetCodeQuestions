/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    
    let n = nums.length
    let answer = []
    
    let compareFn = (a,b) => {
        if (a<b){
            return -1
        }
        else if (a>b){
            return 1
        }
        else{
            return 0
        }
    }
    
    nums.sort(compareFn)
    
    let i = 0
    while (i < n-1){
        let j = i + 1
        let k = n - 1
        
        if (nums[i] > 0){
            i += 1
            continue
        }
        
        while (j < k){
            let sum_ = nums[i] + nums[j] + nums[k]
            
            if (sum_ == 0){
                answer.push([nums[i], nums[j], nums[k]])
                
                while (nums[j] === nums[j+1]){
                    j += 1
                }
                
                while (nums[k] === nums[k-1]){
                    k -= 1
                }
                
                j += 1
                k -= 1
                 
            }
            else if (sum_ > 0){
                k -= 1
            }
            else{
                j += 1
            }
        }
        
        while (i < n - 1 && nums[i] === nums[i+1]){
            i += 1
        }
        
        i += 1
    }
    
    return answer
};