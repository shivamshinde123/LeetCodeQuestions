/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    
    // Approach 1
    // let words =  s.trim().split(" ")
    // let last_word = words[words.length-1]
    // return last_word.length
    words = s.trim().split(" ")
    for (let i = words.length-1; i>-1; i--){
        if (words[i] != " "){
            return words[i].length
        }
    }
};