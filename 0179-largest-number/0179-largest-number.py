class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        nums = map(str,nums)
        
        nums = sorted(nums, key=CustomSmallerNumber)[::-1]
        
        answer = ''.join(nums)
        
        if answer[0] == "0":
            return "0"
        else:
            return answer
    

class CustomSmallerNumber(str):
    def __lt__(self, other):
        return self + other < other + self
    

        