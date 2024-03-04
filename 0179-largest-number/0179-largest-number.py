class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        if len(nums) == 1:
            return str(nums[0])
        
        
        nums = sorted(nums, key=CustomSmallerNumber)[::-1]
        
        answer = ''.join(map(str,nums))
        
        if answer[0] == "0":
            return "0"
        else:
            return answer
    

class CustomSmallerNumber(str):
    def __lt__(self, other):
        return self + other < other + self
    

        