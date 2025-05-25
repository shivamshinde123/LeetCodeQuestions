class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Approach 1
        # return len(nums) > len(set(nums))

        count = Counter(nums)

        for num in count.values():
            if num > 1:
                return True

        return False