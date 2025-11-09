class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = -1
        n = len(nums)

        # Step 1: find the breakpoint 
        for i in range(n - 2, -1 , -1):
            if nums[i] < nums[i+1]:
                index = i
                break

        # If no breakpoint - default to the first array
        if index == -1:
            nums.reverse()
            return

        # If breakpoint is found, swap element at index and the element just greater than it after.
        for i in range(n-1, index, -1):
            if nums[i] > nums[index]:
                nums[i], nums[index] = nums[index], nums[i]
                break

        # Sort the array after index
        nums[index+1:] = reversed(nums[index+1:])