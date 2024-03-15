/**
 * @param {number[]} nums
 * @return {number}
 */
var triangleNumber = function(nums) {
    let n = nums.length
    let count = 0
    
    if (n < 3){
        return 0
    }
    
    nums.sort((a,b)=>{
        if (a < b){
            return -1
        }
        
        else if (a > b){
            return 1
        }
        
        else{
            return 0
        }
    })
    
    for (let i = 0; i < n; i++){
        
        let left = 0
        let right = i - 1
        
        while (left < right){
            
            if (nums[left] + nums[right] > nums[i]){
                count += (right - left)
                right -= 1
            }
            else{
                left += 1
            }
        }
    }
    
    return count
    
};