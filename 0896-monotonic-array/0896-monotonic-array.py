class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        if nums[-1] > nums[0]:
            for i in range(len(nums)-1):
                if nums[i+1] - nums[i] < 0:
                    return False
                
        else:
            for i in range(len(nums)-1):
                if nums[i+1] - nums[i] > 0:
                    return False
                
        return True