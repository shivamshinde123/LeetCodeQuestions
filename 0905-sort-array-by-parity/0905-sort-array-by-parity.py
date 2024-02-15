class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        # Approach 1
        # answer = list()
        # for item in nums:
        #     if item % 2 == 0:
        #         answer.insert(0, item)
        #     else:
        #         answer.append(item)

        # return answer

        # Approach 2: Two pointers approach
        i, j = 0, 0
        while j < len(nums):
            if nums[j] % 2 == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
        
        return nums