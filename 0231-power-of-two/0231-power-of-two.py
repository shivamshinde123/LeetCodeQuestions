class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if (n % 2 == 1 and n > 1) or (n==0):
            return False
        
        if n == 1:
            return True
        
        if self.isPowerOfTwo(n/2):
            return True
        
        