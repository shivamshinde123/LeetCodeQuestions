/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function(matrix, target) {
  
    let m = matrix.length
    let n = matrix[0].length
    
    let left = 0
    let right = m * n - 1
    
    while (left <= right){
        let mid = Math.floor((left + right) / 2)
        
        let mid_row = Math.floor(mid / n)
        let mid_col = mid % n
        
        if (matrix[mid_row][mid_col] == target){
            return true
        }
        
        if (matrix[mid_row][mid_col] < target){
            left = mid + 1
        }
        
        if (matrix[mid_row][mid_col] > target){
            right = mid - 1
        }
    }
    
    return false
};