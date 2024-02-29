class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        nums.sort()
        if (nums[-1] > 0 and nums[-2] == 0) or (nums[-2] < 0 and nums[-1] == 0):
            return (nums[0] - 1)* (nums[1] - 1)
        else:
            return (nums[-1] - 1)* (nums[-2] - 1)
        
        
        
        
        
        