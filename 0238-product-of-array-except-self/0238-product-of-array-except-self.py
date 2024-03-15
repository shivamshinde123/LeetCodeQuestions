class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        before = [1] * n # multiplication of elements before current element
        after = [1] * n # multiplication of elements after current element
        
        for i in range(1, n):
            before[i] = before[i - 1] * nums[i - 1]
            
        for i in range(n-2, -1, -1):
            after[i] = after[i + 1] * nums[i + 1]
            
        answer = [before[i] * after[i] for i in range(n)]
        
        return answer