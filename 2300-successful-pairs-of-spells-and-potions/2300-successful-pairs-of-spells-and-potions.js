/**
 * @param {number[]} spells
 * @param {number[]} potions
 * @param {number} success
 * @return {number[]}
 */
var successfulPairs = function(spells, potions, success) {
    
    let n = spells.length
    let m = potions.length
    
    let answer = new Array(n)
    
    potions.sort((a,b)=>{
        if (a<b){
            return -1
        }
        else if (a>b){
            return 1
        }
        else{
            return 0
        }
    })
    
    for (let i = 0; i < n; i++){
        
        let left = 0
        let right = m - 1
        
        while (left <= right){
            
            let mid = Math.floor((left + right) / 2)
            
            if (potions[mid] * spells[i] >= success){
                right = mid - 1
            }
            else {
                left = mid + 1
            }
        }
        
        answer[i] = m - left
    }
    
    return answer
};