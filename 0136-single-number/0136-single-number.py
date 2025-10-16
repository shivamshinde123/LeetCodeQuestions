class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # Approach 1: Using maps
        # counts = dict()

        # for i in range(len(nums)):
        #     if nums[i] not in counts:
        #         counts[nums[i]] = 1
        #     else:
        #         counts[nums[i]] += 1

        # for key in counts.keys():
        #     if counts[key] != 2:
        #         return key

        # Approach 2: Using XOR
        xor = 0
        for item in nums:
            xor ^= item

        return xor