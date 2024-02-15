class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        middle = 0

        ## Finding the target
        while left <= right:
            middle = (left + right) // 2

            if target == nums[middle]:
                return middle

            if target > nums[middle]:
                left = middle + 1
            
            if target < nums[middle]:
                right = middle - 1


        """
        If the target is not found then we will find the index in list where it fits perfectly 
        """
        # Approach 1(Longer)
        # for i in range(len(nums)-1):
        #     if nums[i] <= target < nums[i+1]:
        #         return i + 1
        
        # if target < nums[0]:
        #     return 0
        
        # if target >= nums[-1]:
        #     return len(nums)

        # Approach 2(Shorter)
        return left