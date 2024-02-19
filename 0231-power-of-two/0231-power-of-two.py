class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        # Approach 1: recursive approach
#         if n > 1 and n % 2 == 1:
#             return False
#         elif n == 0:
#             return False
#         elif n == 1:
#             return True
        
#         if self.isPowerOfTwo(n/2):
#             return True
        
        # Approach 2: bitwise and operation (faster)
        # Following is true when n is the power of two:
        # pow(2, n) & (pow(2, n) - 1) == 0 
        
        return n and not(n & (n-1))
        