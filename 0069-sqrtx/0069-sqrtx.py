class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x-1
        middle = 0

        if x == 0:
            return 0

        while left <= right:
            middle = (left + right)//2

            if middle**2 <= x < (middle+1)**2:
                return middle
            
            if (middle+1)**2 == x:
                return (middle+1)

            if middle**2 < x:
                left = middle + 1
            
            if middle**2 > x:
                right = middle - 1

        return -1