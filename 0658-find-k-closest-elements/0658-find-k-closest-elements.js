/**
 * @param {number[]} arr
 * @param {number} k
 * @param {number} x
 * @return {number[]}
 */
var findClosestElements = function(arr, k, x) {
    let n = arr.length 
    
    let left = 0
    let right = n - 1
    
    while (right - left >= k){
        
        if (Math.abs(arr[left] - x) > Math.abs(arr[right] - x)){
            left += 1
        }
        else{
            right -= 1
        }
    }
    
    return arr.slice(left, right + 1)
};