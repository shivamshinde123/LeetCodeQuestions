class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        left, right = 1, n
        
        while left <= right:
            
            mid = (left + right) // 2
            
            sum = mid* (mid + 1) / 2
            
            if sum == n:
                return mid
                
            if sum < n:
                left  = mid + 1
                
            if sum > n:
                right = mid - 1
                
        return left - 1