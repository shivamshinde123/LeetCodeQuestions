class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        for i in range(len(citations), 0, -1):
            
            val = 0
            for citation in citations:
                if citation >= i:
                    val += 1
                    
            print(f"i: {i} and val: {val}")
            if val >= i:
                return i
            
        return 0
        
            
                
        