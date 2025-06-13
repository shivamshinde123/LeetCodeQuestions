/**
 * @param {string[]} words
 * @return {string[]}
 */
var stringMatching = function(words) {
    
    let result = []

    words.forEach((word, i) => {
    words.forEach((other, j) => {
        if (i !== j && other.includes(word)) {
            if (!result.includes(word)){
                result.push(word)}
            return; // stop checking further
        }
    });
});

    return result
};