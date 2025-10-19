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
        max_sum = curr_sum = nums[0]

        for num in nums[1:]:
            curr_sum = max(num, curr_sum+num)
            max_sum = max(curr_sum, max_sum)

        return max_sum

        


                
