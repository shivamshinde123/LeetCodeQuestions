/**
 * @param {number[]} nums
 * @return {number[]}
 */
var rearrangeArray = function(nums) {

    // Approach 1
    // let answer = [];
    // let pos_stack = [];
    // let neg_stack = [];

    // for (let elem of nums){
    //     if (elem > 0){
    //         pos_stack.push(elem)
    //     }
    //     else{
    //         neg_stack.push(elem)
    //     }
    // }

    // let i = 0
    // while (i < pos_stack.length){
    //     answer.push(pos_stack[i])
    //     answer.push(neg_stack[i])
    //     i++
    // }

    // return answer

    // Approach 2
    let answer = [];
    let pos = 0
    let neg = 1

    for (let elem of nums){
        if (elem > 0){
            answer[pos] = elem
            pos = pos + 2
        }
        else{
            answer[neg] = elem
            neg = neg + 2
        }
    }

    return answer
};