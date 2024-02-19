/**
 * @param {string[]} words
 * @return {string[]}
 */
var findWords = function(words) {
    
    let first_row = new Set("qwertyuiop");
    let second_row = new Set("asdfghjkl");
    let third_row = new Set("zxcvbnm");
    
    let answer = [];
    
    let check_presence = (row, word) => {
        
        for (let char of word){
            if (!(row.has(char.toLowerCase()))){
                return false
            }
        }
        
        return true
    }
    
    for (let word of words){
        
        if (check_presence(first_row, word) || check_presence(second_row, word) || check_presence(third_row, word)){
            answer.push(word)
        }
        
    }
    
        
    return answer     
    
};