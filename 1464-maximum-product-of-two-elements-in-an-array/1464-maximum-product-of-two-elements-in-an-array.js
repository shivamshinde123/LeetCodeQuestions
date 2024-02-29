/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function(nums) {
    
//     let merge_two_arr = (arr1, arr2) => {
//         let i = 0
//         let j = 0
        
//         merged_arr = []
//         while (i < arr1.length && j < arr2.length){
//             if (arr1[i] < arr2[j]){
//                 merged_arr.push(arr1[i])
//                 i += 1
//             }
//             else{
//                 merged_arr.push(arr2[j])
//                 j += 1
//             }
//         }
        
        
//         while (i < arr1.length){
//         merged_arr.push(arr1[i])
//         i += 1
//         }
    
//         while (j < arr2.length){
//             merged_arr.push(arr2[j])
//             j += 1
//         }
//     }
    
   
//     let mergesort = (arr) => {
        
//         middle_index = Math.round(arr.length / 2)
        
//         left = arr.slice(0, middle_index)
//         right = arr.slice(middle_index)
        
//         left = mergesort(left)
//         right = mergesort(right)
        
//         return merge_two_arr(left, right)
                
//     }
    
//     sorted_arr = mergesort(nums)
    
    function compareFn(a, b) {
        if (a<b) {
            return -1;
        } 
        else if (a>b) {
            return 1;
        }
        else {
        return 0;
        }
    }
    
    nums.sort(compareFn)
    
    if ((nums[nums.length-2] === 0 && nums[nums.length-1] > 0) || (nums[nums.length-2] <  0 && nums[nums.length-1] == 0)){
        return (nums[0] - 1) * (nums[1] - 1)
    }
    else{
        return (nums[nums.length-2] - 1) * (nums[nums.length-1] - 1) 
    }
    
    
};