class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = list()
        for i in range(2*n):
            if i < n:
                ans.append(nums[i])
            else:
                ans.append(nums[i - n])

        return ans


