class Solution:
    def isHappy(self, n: int) -> bool:

        seen = set()
        
        def sq_sum_of_digits(n):
            sq_sum = 0
            while n != 0:
                digit = n % 10
                sq_sum += digit**2
                n //= 10
            return sq_sum

        while True:
            sq_sum = sq_sum_of_digits(n)
            if sq_sum == 1:
                return True
            elif sq_sum in seen:
                return False
            seen.add(sq_sum)
            n = sq_sum

            
        
        return False