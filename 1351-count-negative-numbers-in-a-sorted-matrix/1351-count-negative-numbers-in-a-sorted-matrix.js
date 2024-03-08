/**
 * @param {number[][]} grid
 * @return {number}
 */
var countNegatives = function(grid) {
    
    let countNeg = (arr) => {
        
        /*
        This function will find the index of first negative number in an array and using it will find the count of total
        negative numbers in the same array. Note that at the end of while loop, left_index position will be the index of first
        negative number in an array.
        */
        
        let n = arr.length
        let left_index = 0
        let right_index = n - 1
        
        while (left_index <= right_index) {
            
            let mid_index = Math.floor((left_index + right_index) / 2)
            let mid_value = arr[mid_index]
            
            if (mid_value >= 0){
                left_index = mid_index + 1
            }
            else {
                right_index = mid_index - 1
            }
        }
        
        return arr.length - left_index
    }
    
    let answer = 0
    for (let arr of grid){
        answer += countNeg(arr)
    }
    
    return answer
};