/**
 * @param {string} s
 * @param {string} t
 * @return {number}
 */
var appendCharacters = function(s, t) {
    
    let n = t.length;
    let m = s.length;

    let i = 0;
    let j = 0;

    while (i < n && j < m){
        if (t[i] == s[j]){
            i++;
            j++
        }
        else{
            j++
        }
    }

    return n - i
};