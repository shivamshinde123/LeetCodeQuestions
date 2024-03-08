/**
 * @param {character[]} letters
 * @param {character} target
 * @return {character}
 */
var nextGreatestLetter = function(letters, target) {
    let n = letters.length
    let left_index = 0
    let right_index = n - 1
    
    if (target < letters[left_index] || target >= letters[right_index]){
        return letters[left_index]
    }
    
    while (left_index <= right_index) {
        
        let mid_index = Math.floor((left_index + right_index) / 2)
        let mid_value = letters[mid_index]
        
        if (target < mid_value){
            right_index = mid_index - 1
        }
        if (target >= mid_value){
            left_index = mid_index + 1
        }
    }
    
    return letters[left_index]
};