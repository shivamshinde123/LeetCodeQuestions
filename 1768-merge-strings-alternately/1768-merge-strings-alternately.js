/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var mergeAlternately = function(word1, word2) {
    let i = 0;
    let j = 0;
    let common_string = ""
    while (i < word1.length && j < word2.length){
        common_string += word1[i]
        common_string += word2[j]
        i += 1
        j += 1
    }
    
    while (i < word1.length){
        common_string += word1[i]
        i += 1
    }
    
    while (j < word2.length){
        common_string += word2[j]
        j += 1
    }
    
    return common_string
};