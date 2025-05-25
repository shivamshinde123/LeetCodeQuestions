class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Approach 1
        # return len(nums) > len(set(nums))

        # Approach 2
        count = Counter(nums)

        for num in count.values():
            if num > 1:
                return True

        return False

        # Approach 3
        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         return True
        #     seen.add(num)
        
        # return False

        # Approach 4
        # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return True
            
        # return False