class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        
        # Approach 1
        # answer = [0]*len(nums) # if we don't initialize the array, we will get out of index error
        # i, j = 0, 1

        # for num in nums:
        #     if num % 2 == 0:
        #         answer[i] = num
        #         i += 2
        #     else:
        #         answer[j] = num
        #         j += 2

        # return answer

        # Approach 2: Two pointer solution
        even = 0
        odd = 1

        while (even < len(nums)) and (odd < len(nums)):
            while (even < len(nums)) and (nums[even] % 2 == 0):
                even += 2

            while (odd < len(nums)) and (nums[odd] % 2 != 0):
                odd += 2

            if (even < len(nums)) and (odd < len(nums)):
                nums[even], nums[odd] = nums[odd], nums[even]
                even += 2
                odd += 2

        return nums

