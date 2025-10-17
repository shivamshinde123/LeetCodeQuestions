class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Brute Force Approach
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # hashmap
        hashmap = dict()

        for index, value in enumerate(nums):
            if (target - value) in hashmap:
                return [index, hashmap[target - value]]
            
            hashmap[value] = index

        
