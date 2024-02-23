class Solution:
    def countOdds(self, low: int, high: int) -> int:
        
        # Approach 1: Time Limit Exceeded
#         def isOdd(num):
#             return num % 2 == 1
        
#         count = 0
#         for num in range(low, high+1):
#             if isOdd(num):
#                 count += 1
        
#         return count

        # Approach 2
        def isOdd(num):
            return num % 2 == 1
        
        diff = high - low
        
        if not isOdd(low) and not isOdd(high):
            return diff // 2
        else:
            return diff // 2 + 1