class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        # Approach 1: Time Limit Exceeded
#         if n == 0:
#             return 1
        
#         answer = 1
        
#         if n > 0:
#             for i in range(n):
#                 answer *= x
#             return answer
#         else:
#             for i in range(-n):
#                 answer *= x
#             return 1 / answer


        # Approach 2
        if n >= 0:
            return self.helper(x, n)
        else:
            return 1 / self.helper(x, -n)


    def helper(self, x, n):
        
        if n == 0:
            return 1
        
        temp = self.myPow(x, n // 2)
        
        def isEven(n):
            return floor(n % 2) == 0
        
        if isEven(n):
            return temp * temp
        else:
            return temp * temp * x
        
            
    
    
        
        