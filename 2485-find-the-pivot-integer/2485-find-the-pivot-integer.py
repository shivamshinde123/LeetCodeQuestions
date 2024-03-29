class Solution:
    def pivotInteger(self, n: int) -> int:
        
        # sum(1 to x, both included) = sum(x to n, both included)
        # This implies that x**2 = n * (n + 1) / 2
        # So basically we want to find the square root of n * (n + 1) / 2
        
        sum = int(n * (n + 1) / 2)
        
        left, right = 1, sum
        
        while left <= right:
            
            mid = (left + right) // 2
            
            if mid**2 == sum:
                return mid
            
            if mid**2 < sum:
                left = mid + 1
                
            if mid**2 > sum:
                right = mid - 1
                
        return -1
        