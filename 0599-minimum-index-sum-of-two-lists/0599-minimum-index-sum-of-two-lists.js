/**
 * @param {string[]} list1
 * @param {string[]} list2
 * @return {string[]}
 */
var findRestaurant = function(list1, list2) {
    let index_sum = Infinity
    let common_string = []
    
    for (let i = 0; i< list1.length; i++){
        if (list2.includes(list1[i])){
            j = list2.indexOf(list1[i])
            
            if (i+j < index_sum){
                index_sum = i + j
                common_string.length = 0
                common_string.push(list1[i])
            }
            else if (i + j === index_sum){
                common_string.push(list1[i])
            }
        }
    }
    
    return common_string
};