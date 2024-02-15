class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        # Approach 1: Time Limit Exceeded
        # for j in range(len(nums)):
        #     for i in range(j+1,min(j+1+k, len(nums))):
        #         if nums[i] == nums[j]:
        #             return True

        # Approach 2
        d = dict()

        for index, value in enumerate(nums):
            if value in d and abs(index - d[value]) <= k:
                return True
            else:
                d[value] = index
            
        return False
        

        