class Solution:
    def reverse(self, x: int) -> int:
        
        pos = x > 0
        
        if not pos:
            x = -x 

        # works with positive integers
        def get_digit(x, index):
            return x // (10**index) % 10
        
        reverse = 0
        n = len(str(x))
        
        for i in range(n):
            reverse += get_digit(x, i) * (10**(n-1-i))
            
        if reverse < -1*2**31 or reverse > (2**31-1):
            return 0
        
        if pos:
            return reverse
        else:
            return -1 * reverse
        
        