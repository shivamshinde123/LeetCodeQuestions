class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if n > 1 and n % 2 == 1:
            return False
        elif n == 0:
            return False
        elif n == 1:
            return True
        
        if self.isPowerOfTwo(n/2):
            return True
        
        