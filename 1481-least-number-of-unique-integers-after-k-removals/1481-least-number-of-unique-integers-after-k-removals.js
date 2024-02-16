/**
 * @param {number[]} arr
 * @param {number} k
 * @return {number}
 */
var findLeastNumOfUniqueInts = function(arr, k) {
    
    // finding the frequencay of each of element in arr
    let arr_elem_freq = {}
    
    for (let elem of arr){
        if (!(elem in arr_elem_freq)){
            arr_elem_freq[elem] = 1
        }
        else{
            arr_elem_freq[elem] += 1
        }
    }
    
    // sorting the arr_elem_freq object using the frequency of occurence in ascending order
    // Object.fromEntries convert array to object
    // Object.entries convert object to array
    let sorted_arr_elem_freq = Object.entries(arr_elem_freq).sort(function (a,b){return (a[1] < b[1] ? -1 : 1)})

    
    for (let item of sorted_arr_elem_freq){
        if (k > 0){
            val = item[1]
            if (val <= k){
                k -= val
                item[1] = 0
            }
            else{
                item[1] -= k
                k = 0
            }
        }
    }
    
    transformed_arr = []
    for (let item of sorted_arr_elem_freq){
        if (item[1] !== 0){
            transformed_arr.push(item[0])
        }
    }
    
    return transformed_arr.length
    
};
