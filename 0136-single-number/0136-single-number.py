class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        # Approach 1
        # for i in range(len(nums)):
        #     num = nums[i]
        #     nums.remove(num)
        #     if num not in nums:
        #         return num
        #     nums.insert(i, num)

        # Approach 2
        unique_nums = list(set(nums))
        return 2*sum(unique_nums) - sum(nums)
