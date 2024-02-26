class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        # Using a stack
#         stack = list()
        
#         for i in range(len(prices)):
            
#             while stack and prices[stack[-1]] >= prices[i]:
#                 prices[stack.pop()] -= prices[i]
                
#             stack.append(i)
            
#         return prices
    
        # Using an array
        
        def findLesserValue(index):
            for val in prices[index+1:]:
                if val <= prices[index]:
                    return val
            
            return 0
        
        for i in range(len(prices)-1):
            prices[i] -= findLesserValue(i)
        
        return prices
        
        
            
            