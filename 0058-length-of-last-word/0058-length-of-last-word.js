/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    let words =  s.trim().split(" ")
    let last_word = words[words.length-1]
    return last_word.length
};