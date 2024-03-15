class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        n = len(spells)
        m = len(potions)
        
        answer = list()
        potions.sort()
        for i in range(n):
            
            left, right = 0, m - 1
            
            while left <= right:
                
                mid = (left + right) // 2
                
                if potions[mid] * spells[i] >= success:
                    right = mid - 1
                
                else:
                    left = mid + 1
                    
            answer.append(m - left)
            
        return answer