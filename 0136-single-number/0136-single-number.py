class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        counts = dict()

        for i in range(len(nums)):
            if nums[i] not in counts:
                counts[nums[i]] = 1
            else:
                counts[nums[i]] += 1

        for key in counts.keys():
            if counts[key] != 2:
                return key