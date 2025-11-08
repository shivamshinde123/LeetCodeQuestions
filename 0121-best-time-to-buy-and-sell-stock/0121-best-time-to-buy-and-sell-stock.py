class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    
        # Brute force solution - TIME LIMIT EXCEEDED
        # n = len(prices)
        # max_profit = - float('inf')
        # for i in range(n):
        #     for j in range(i+1, n):
        #         profit = prices[j] - prices[i]

        #         if profit > max_profit:
        #             max_profit = profit

        # if max_profit < 0:
        #     return 0
                
        # return max_profit

        # Optimal approach
        max_profit = 0
        min_price = float('inf')

        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]

            profit = prices[i] - min_price
            if profit > max_profit:
                max_profit = profit

        if max_profit < 0:
            return max_profit

        return max_profit


