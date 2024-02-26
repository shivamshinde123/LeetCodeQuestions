class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        # Using a stack
        stack = list()
        
        for i in range(len(prices)):
            
            while stack and prices[stack[-1]] >= prices[i]:
                prices[stack.pop()] -= prices[i]
                
            stack.append(i)
            
        return prices
            