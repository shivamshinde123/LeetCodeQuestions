class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute force approach
        # n = len(nums)
        # indices = list()
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if nums[i] + nums[j] == target:
        #             indices.append(i)
        #             indices.append(j)

        # return indices

        # HashMap (val -> index)

        hashmap = dict()

        for index, num in enumerate(nums):
            diff = target - num

            if diff in hashmap:
                return [hashmap[diff], index]
            
            hashmap[num] = index

