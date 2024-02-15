class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        maxP = 0
        n = len(nums)
        if n < 3:
            return -1
        
        nums.sort(reverse=True)
        
        for i in range(n-2):
            if nums[i] < sum(nums[i+1:]):
                maxP = max(maxP, sum(nums[i:]))
                break
                
        if maxP == 0:
            return -1
        else: return maxP