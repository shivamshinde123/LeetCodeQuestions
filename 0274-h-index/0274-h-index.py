class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        for i in range(len(citations), 0, -1):
            
            val = 0
            for citation in citations:
                if citation >= i:
                    val += 1
                    
            if val >= i:
                return i
            
        return 0 # When h_index is not valid for researcher i.e., researchers doesn't have any published work
    
    
        
            
                
        