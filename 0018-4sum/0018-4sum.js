/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[][]}
 */
var fourSum = function(nums, target) {
    let n = nums.length
    let answer = []
    
    let compareFn = (a,b) => {
        if (a < b){
            return -1
        }
        else if (a > b){
            return 1
        }
        else{
            return 0
        }
    }
    
    nums.sort(compareFn)
    let i = 0
    
    while (i < n- 2){
        let j = i + 1
        
        while (j < n - 1){
            let k = j + 1
            let l = n - 1
            
            while (k < l){
                let sum_ = nums[i] + nums[j] + nums[k] + nums[l]
                
                if (sum_ === target){
                    answer.push([nums[i], nums[j], nums[k], nums[l]])
                    
                    while (nums[k] === nums[k+1]){
                        k += 1
                    }
                
                    while (nums[l] === nums[l-1]){
                        l -= 1
                    }
                
                    k += 1
                    l -= 1
                }
                else if (sum_ > target){
                    l -= 1
                }
                else {
                    k += 1
                }
            }
            
            while (j < n - 1 && nums[j] === nums[j+1]){
                j += 1
            }
            
            j += 1
            
        }
        
        while (i < n - 2 && nums[i] === nums[i+1]){
            i += 1
        }
        
        i += 1
    }
    
    return answer
};