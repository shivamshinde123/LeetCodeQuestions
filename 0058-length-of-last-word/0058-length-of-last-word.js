/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    let n = s.length;
    // Creating two variables - one for tracking index and one for tracking length
    let i = n - 1;
    let length = 0;

    while (s[i] == " "){
        i--;
    }

    while (i >= 0 && s[i] != 0){
        i--;
        length++;
    }

    return length
};