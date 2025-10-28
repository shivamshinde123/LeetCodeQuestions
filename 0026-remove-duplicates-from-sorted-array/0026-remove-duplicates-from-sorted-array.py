class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # Brute force approach:Use set to get the unique elements and then put them in the first k positions

        # Optimal approach
        i, j = 0, 1
        n = len(nums)
        for j in range(1, n):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        
        return i + 1