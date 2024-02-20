class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Approach 1 (Linear Search)
        # for i in list(range(len(nums)+1)):
        #     if i not in nums:
        #         return i
        # return -1

        ## Approach 2 (sum of numbers from 0 to n minus sum of numbers in given array)
        # n = len(nums)
        # sum_of_nums = sum(nums)
        # return int(n*(n+1)/2- sum_of_nums)

        ## Approach 3 (Binary Search)
        left = 0
        right = len(nums) - 1
        middle = 0

        nums = sorted(nums)

        while left <= right:
            middle = (left + right)//2

            if nums[middle] != middle:
                right = middle - 1
            else:
                left = middle + 1

        return left