class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        indices = list()
        for i in range(n):
            for j in range(i+1,n):
                if nums[i] + nums[j] == target:
                    indices.append(i)
                    indices.append(j)

        return indices