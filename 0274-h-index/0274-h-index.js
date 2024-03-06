/**
 * @param {number[]} citations
 * @return {number}
 */
var hIndex = function(citations) {
    
    citations.sort((a,b)=>{
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
    
    n = citations.length
    for (let citation of citations){
        if (citation < n){
            n -= 1
        }
    }
    
    return n
};