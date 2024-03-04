class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        
        if len(nums) < 2:
            return 0
        
        nums.sort()
        
        max_diff = -math.inf
        
        for i in range(len(nums)-1):
            local_diff = abs(nums[i] - nums[i+1])
            max_diff = max(local_diff, max_diff)
            
        return max_diff