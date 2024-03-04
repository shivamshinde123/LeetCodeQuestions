class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        
        max_diff = 0
        for i in range(len(nums)-1):
            local_diff = abs(nums[i] - nums[i+1])
            max_diff = max(local_diff, max_diff)
            
        return max_diff