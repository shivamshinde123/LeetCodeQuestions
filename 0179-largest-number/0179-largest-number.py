class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        if len(nums) < 2:
            return str(nums[0])
        
        
        nums = sorted(nums, key=CustomSmallerNumber)[::-1]
        
        answer = ''.join(map(str,nums))
        
        return str(int(answer))
    

class CustomSmallerNumber(str):
    def __lt__(self, other):
        return self + other < other + self
    

        