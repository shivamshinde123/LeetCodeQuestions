class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # Brute force - Time Limit Exceeding
        # n = len(nums)
        # max_sum = float('-inf')

        # for i in range(n):
        #     curr_sum = 0
        #     for j in range(i, n):
        #         curr_sum += nums[j]
        #         if curr_sum > max_sum:
        #             max_sum = curr_sum

        # return max_sum

        # Approach 2 - Kadane Algorithm
        max = - float('inf')
        sum = 0

        for i in range(len(nums)):

            sum += nums[i]

            if sum > max:
                max = sum

            if sum < 0:
                sum = 0

            
        # if max < 0: max = 0

        return max

        


                
