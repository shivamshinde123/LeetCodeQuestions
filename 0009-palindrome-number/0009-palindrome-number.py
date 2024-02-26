class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        digits = list()
        
        def get_digit(number, n):
            return number // 10**n % 10
        
        for i in range(len(str(x))-1, -1, -1):
            digits.append(get_digit(x,i))
        
        print(digits)
        x_reverse = 0
        for i in range(len(digits)):
            x_reverse += digits[i] * 10**i
            
        return x == x_reverse
            
        