class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        def get_digit(number, n):
            return number // (10**n) % 10
        
        n = len(str(x))
        reverse = 0
        
        for i in range(n):
            reverse += get_digit(x, i) * 10**(n-1-i)
            
        return x == reverse
            
        