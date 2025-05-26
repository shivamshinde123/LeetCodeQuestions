/**
 * @param {number[]} arr
 * @return {number[]}
 */
var replaceElements = function(arr) {
    let n = arr.length;
    let res = new Array(n);
    let right_max = -1;

    for (let i=n-1; i>=0; i--){
        res[i] = right_max;
        right_max = Math.max(right_max, arr[i]);
    }

    return res;
};