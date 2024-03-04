/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    let ana = {}
    
    let sorting_fun = (strs) => {
        return strs.split('').sort().join('')
        
    }
    
    for (let element of strs){
        rearranged_ele = sorting_fun(element)
        
        if (ana[rearranged_ele] === undefined){
            ana[rearranged_ele] = new Array()
            ana[rearranged_ele].push(element)
        }
        else{
            ana[rearranged_ele].push(element)
        }
    }

    
    return Object.values(ana)
};