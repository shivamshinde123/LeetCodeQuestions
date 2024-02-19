/**
 * @param {string} text
 * @param {string} brokenLetters
 * @return {number}
 */
var canBeTypedWords = function(text, brokenLetters) {
    let words = text.split(" ")
    let num_of_words = words.length
    
    for (let word of words){
        for (let char of word){
            if (brokenLetters.includes(char)){
                num_of_words -= 1
                break
            }
        }
    }
    
    return num_of_words
};